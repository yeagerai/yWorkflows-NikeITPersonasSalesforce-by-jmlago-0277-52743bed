
import pytest
from fastapi.testclient import TestClient
from your_component_module import NikeITPersonasSalesforce, nike_it_personas_salesforce_app, NikeITPersonasInput, NikeITPersonasOutput

client = TestClient(nike_it_personas_salesforce_app)
