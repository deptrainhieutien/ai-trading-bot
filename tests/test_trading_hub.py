"""
Tests for Trading Hub 3.0 Quant Master Engine.
"""
import pytest
from trading_hub_engine import TradingHubEngine

def test_engine_init():
    engine = TradingHubEngine()
    assert engine.bias == "Bullish"
    assert engine.structure_type == "Choch with IDM"

def test_mother_bar_protection():
    engine = TradingHubEngine(filter_isb=True)
    engine.update_mother_bar(100.0, 90.0)
    # Inside bar should be ignored for pullback
    isb = engine.update_mother_bar(95.0, 92.0)
    assert isb is True

def test_process_candle():
    engine = TradingHubEngine()
    res = engine.process_candle(100.0, 105.0, 98.0, 102.0)
    assert res["bias"] == "Bullish"
    assert res["mother_high"] == 105.0
