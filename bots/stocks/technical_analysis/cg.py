from datetime import datetime, timedelta

import numpy as np
from matplotlib import pyplot as plt

import bots.config_discordbot as cfg
import bots.helpers
from bots.config_discordbot import logger
from bots.helpers import image_border
from gamestonk_terminal.common.technical_analysis import momentum_model
from gamestonk_terminal.config_plot import PLOT_DPI
from gamestonk_terminal.helper_funcs import plot_autoscale


def cg_command(ticker="", length="14", start="", end=""):
    """Displays chart with centre of gravity [Yahoo Finance]"""

    # Debug
    if cfg.DEBUG:
        logger.debug(
            "ta-cg %s %s %s %s",
            ticker,
            length,
            start,
            end,
        )

    # Check for argument
    if ticker == "":
        raise Exception("Stock ticker is required")

    if start == "":
        start = datetime.now() - timedelta(days=365)
    else:
        start = datetime.strptime(start, cfg.DATE_FORMAT)

    if end == "":
        end = datetime.now()
    else:
        end = datetime.strptime(end, cfg.DATE_FORMAT)

    if not length.lstrip("-").isnumeric():
        raise Exception("Number has to be an integer")
    length = float(length)

    ticker = ticker.upper()
    df_stock = bots.helpers.load(ticker, start)
    if df_stock.empty:
        raise Exception("Stock ticker is invalid")

    # Retrieve Data
    df_stock = df_stock.loc[(df_stock.index >= start) & (df_stock.index < end)]
    df_close = df_stock["Adj Close"]
    df_close.columns = ["values"]
    df_ta = momentum_model.cg(df_close, length)

    # Output Data
    fig, axes = plt.subplots(2, 1, figsize=plot_autoscale(), dpi=PLOT_DPI)
    ax = axes[0]
    ax.set_title(f"{ticker} Centre of Gravity")
    ax.plot(df_stock.index, df_stock["Adj Close"].values, "k", lw=1)
    ax.set_xlim(df_stock.index[0], df_stock.index[-1])
    ax.set_ylabel("Share Price ($)")
    ax.grid(b=True, which="major", color="#666666", linestyle="-")

    ax2 = axes[1]
    ax2.plot(df_ta.index, df_ta.values, "b", lw=2, label="CG")
    # shift cg 1 bar forward for signal
    signal = df_ta.values
    signal = np.roll(signal, 1)
    ax2.plot(df_ta.index, signal, "g", lw=1, label="Signal")
    ax2.set_xlim(df_stock.index[0], df_stock.index[-1])
    ax2.grid(b=True, which="major", color="#666666", linestyle="-")

    plt.gcf().autofmt_xdate()
    fig.tight_layout(pad=1)
    plt.legend()
    imagefile = "ta_cg.png"
    plt.savefig(imagefile)

    imagefile = image_border(imagefile)

    return {
        "title": f"Stocks: Center-of-Gravity {ticker}",
        "imagefile": imagefile,
    }
