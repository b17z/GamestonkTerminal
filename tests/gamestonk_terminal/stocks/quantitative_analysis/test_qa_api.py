# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY

# IMPORTATION INTERNAL
from gamestonk_terminal.helper_classes import ModelsNamespace as _models
from gamestonk_terminal.stocks.quantitative_analysis import qa_api


def test_models():
    assert isinstance(qa_api.models, _models)
