from src.experiment import Experiment
from pytest import approx


def test_p_2_heads():
    e = Experiment()
    #assert e.p_2_heads(10000) == approx(0.5, rel=1e-2)

def test_p_pattern():
    e = Experiment()
    assert e.p_pattern('HHTHTT') == approx(1/(2**6), rel=1e-2)
    assert e.p_pattern('HHTHTTTT') == approx(1/(2**8), rel=1e-2)