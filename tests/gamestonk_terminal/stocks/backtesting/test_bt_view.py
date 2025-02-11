# IMPORTATION STANDARD
from datetime import datetime

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL
from gamestonk_terminal.stocks import stocks_helper
from gamestonk_terminal.stocks.backtesting import bt_view


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("period1", "1598220000"),
            ("period2", "1635980400"),
        ],
    }


@pytest.mark.vcr
@pytest.mark.record_stdout
def test_display_simple_ema(mocker):
    yf_download = stocks_helper.yf.download

    def mock_yf_download(*args, **kwargs):
        kwargs["threads"] = False
        return yf_download(*args, **kwargs)

    mocker.patch("yfinance.download", side_effect=mock_yf_download)

    # MOCK VISUALIZE_OUTPUT
    mocker.patch(
        target="gamestonk_terminal.helper_classes.TerminalStyle.visualize_output"
    )

    ticker = "PM"
    start = datetime.strptime("2020-12-01", "%Y-%m-%d")
    end = datetime.strptime("2020-12-02", "%Y-%m-%d")
    df_stock = stocks_helper.load_ticker(ticker=ticker, start_date=start, end_date=end)
    bt_view.display_simple_ema(
        ticker=ticker,
        df_stock=df_stock,
        ema_length=2,
        spy_bt=True,
        no_bench=False,
        export=False,
    )


@pytest.mark.vcr
@pytest.mark.record_stdout
def test_display_ema_cross(mocker):
    yf_download = stocks_helper.yf.download

    def mock_yf_download(*args, **kwargs):
        kwargs["threads"] = False
        return yf_download(*args, **kwargs)

    mocker.patch("yfinance.download", side_effect=mock_yf_download)

    # MOCK VISUALIZE_OUTPUT
    mocker.patch(
        target="gamestonk_terminal.helper_classes.TerminalStyle.visualize_output"
    )

    ticker = "PM"
    start = datetime.strptime("2020-12-01", "%Y-%m-%d")
    end = datetime.strptime("2020-12-02", "%Y-%m-%d")
    df_stock = stocks_helper.load_ticker(ticker=ticker, start_date=start, end_date=end)
    bt_view.display_ema_cross(
        ticker=ticker,
        df_stock=df_stock,
        short_ema=2,
        long_ema=2,
        spy_bt=True,
        no_bench=False,
        shortable=True,
        export=False,
    )


@pytest.mark.vcr
@pytest.mark.record_stdout
def test_display_rsi_strategy(mocker):
    yf_download = stocks_helper.yf.download

    def mock_yf_download(*args, **kwargs):
        kwargs["threads"] = False
        return yf_download(*args, **kwargs)

    mocker.patch("yfinance.download", side_effect=mock_yf_download)

    # MOCK VISUALIZE_OUTPUT
    mocker.patch(
        target="gamestonk_terminal.helper_classes.TerminalStyle.visualize_output"
    )

    ticker = "PM"
    start = datetime.strptime("2020-12-01", "%Y-%m-%d")
    end = datetime.strptime("2020-12-02", "%Y-%m-%d")
    df_stock = stocks_helper.load_ticker(ticker=ticker, start_date=start, end_date=end)
    bt_view.display_rsi_strategy(
        ticker=ticker,
        df_stock=df_stock,
        periods=2,
        low_rsi=2,
        high_rsi=2,
        spy_bt=True,
        no_bench=False,
        shortable=True,
        export=False,
    )
