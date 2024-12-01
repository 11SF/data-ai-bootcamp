import os
import sys
import json
from typing import List
from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine
from google.protobuf.json_format import MessageToDict


def vertex_search_retail_products(
    search_query: str,
) -> List[discoveryengine.SearchResponse]:
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    GCP_PROJECT_ID  = os.environ["GCP_PROJECT_ID"]
    VERTEX_ENGINE = os.environ["VERTEX_SEARCH_ID"]
    APP_LOCATION = os.environ["VERTEX_SEARCH_LOCATION"]
    
    client_options = (
        ClientOptions(api_endpoint=f"{APP_LOCATION}-discoveryengine.googleapis.com")
        if APP_LOCATION != "global"
        else None
    )

    client = discoveryengine.SearchServiceClient(client_options=client_options)
    serving_config = (
        f"projects/{GCP_PROJECT_ID}/locations/{APP_LOCATION}"
        f"/collections/default_collection/engines/{VERTEX_ENGINE}"
        f"/servingConfigs/default_config"
    )

    # Optional - only supported for unstructured data: Configuration options for search.
    # Refer to the `ContentSearchSpec` reference for all supported fields:
    # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest.ContentSearchSpec
    content_search_spec = discoveryengine.SearchRequest.ContentSearchSpec(
        # For information about search summaries, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/get-search-summaries
        summary_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec(
            summary_result_count=5,
            include_citations=True,
            ignore_adversarial_query=True,
            ignore_non_summary_seeking_query=True,
            model_prompt_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelPromptSpec(
                preamble="ค้นหาสินค้าที่มีอยู่ และอธิบายเป็นภาษาไทย"
            ),
            model_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec.ModelSpec(
                version="stable",
            ),
        ),
    )

    # Refer to the `SearchRequest` reference for all supported fields:
    # https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest
    request = discoveryengine.SearchRequest(
        serving_config=serving_config,
        query=search_query,
        page_size=5,
        content_search_spec=content_search_spec,
        query_expansion_spec=discoveryengine.SearchRequest.QueryExpansionSpec(
            condition=discoveryengine.SearchRequest.QueryExpansionSpec.Condition.AUTO,
        ),
        spell_correction_spec=discoveryengine.SearchRequest.SpellCorrectionSpec(
            mode=discoveryengine.SearchRequest.SpellCorrectionSpec.Mode.AUTO
        ),
    )

    response = client.search(request)
    response_dict = MessageToDict(response._pb)
    return response_dict

if __name__ == "__main__":    
    outer_lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
    sys.path.append(outer_lib_path)
    from commons.manage_secret import load_secrets
    load_secrets("vertex_ai_secret.yml")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "sa.json"
    search_query = "คาราบาวแดง"
    results = vertex_search_retail_products(search_query=search_query)
    print(json.dumps(results, indent=4))