import yaml

def test_config_structure():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    # Ensure required sections exist
    for section in ["secrets", "tags", "apps", "cron", "logging"]:
        assert section in config

    # Check secrets placeholders
    assert "github_token" in config["secrets"]
    assert config["secrets"]["github_token"].startswith("${")