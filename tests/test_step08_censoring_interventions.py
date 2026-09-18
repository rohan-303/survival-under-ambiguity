from survival_ambiguity.censoring_interventions import (
    LatentRow, SurvivalRecord, cox_survival, common_support,
    composition_identity, fit_cox, naive_observed_event_risk, observe,
    prediction_discrepancy, recensor, stratified_km,
)


def test_recensor_cannot_create_event_information():
    censored = SurvivalRecord((0.0,), 2, 0)
    assert recensor(censored, 5) == censored
    assert recensor(SurvivalRecord((0.0,), 5, 1), 3) == SurvivalRecord((0.0,), 3, 0)


def test_event_before_artificial_cutoff_remains_event():
    event = SurvivalRecord((0.0,), 2, 1)
    assert recensor(event, 4) == event


def test_finite_composition_identity_and_no_intervention():
    rows = tuple(LatentRow((float(i % 2),), 1 + i, 2 + (i % 3)) for i in range(8))
    assert composition_identity(rows, 3)
    records = tuple(observe(r) for r in rows)
    assert all(recensor(r, 99) == r for r in records)


def test_common_support_mask_excludes_lost_horizons():
    mask = common_support({1: 1.0, 2: .5, 3: .1}, {1: 1.0, 2: .2, 3: 0.0}, [1, 2, 3])
    assert mask == {1: True, 2: True, 3: False}


def test_stratified_km_and_discrepancy_are_deterministic():
    records = (SurvivalRecord((0.0,), 1, 1), SurvivalRecord((0.0,), 3, 0),
               SurvivalRecord((1.0,), 2, 1), SurvivalRecord((1.0,), 3, 1))
    a = stratified_km(records, [1, 2, 3])
    b = stratified_km(records, [1, 2, 3])
    assert a == b and 0 <= a[(0.0,)][1] <= 1
    assert prediction_discrepancy(a, b, {1: True, 2: True, 3: True}) == 0


def test_cox_fit_and_prediction_are_finite():
    records = tuple(SurvivalRecord((float(i % 2),), 1 + (i % 4), int(i % 3 != 0)) for i in range(20))
    beta = fit_cox(records)
    pred = cox_survival(records, beta, [1, 2, 3])
    assert len(beta) == 1 and all(0 < v <= 1 for c in pred.values() for v in c.values())


def test_naive_learner_is_explicitly_different_from_km_on_censoring_fixture():
    records = (SurvivalRecord((0.0,), 1, 1), SurvivalRecord((0.0,), 1, 0),
               SurvivalRecord((0.0,), 4, 0))
    naive = naive_observed_event_risk(records, [1])[(0.0,)][1]
    km = stratified_km(records, [1])[(0.0,)][1]
    assert naive != km
