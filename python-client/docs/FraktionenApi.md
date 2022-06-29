# abfallnavi.FraktionenApi

All URIs are relative to *https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**muellarten**](FraktionenApi.md#muellarten) | **GET** /fraktionen | Müllarten im System
[**muellarten_pro_hausnummer**](FraktionenApi.md#muellarten_pro_hausnummer) | **GET** /hausnummern/{hausnummernId}/fraktionen | Müllarten für Hausnummer
[**muellarten_pro_strasse**](FraktionenApi.md#muellarten_pro_strasse) | **GET** /strassen/{strassenId}/fraktionen | Müllarten für Straßen


# **muellarten**
> [Fraktion] muellarten()

Müllarten im System

Welche Müllarten es im System gibt (z.B. Restabfall, Bioabfall, Papiertonne, Gelbe Tonne, Papiertonne 1100)

### Example


```python
import time
from deutschland import abfallnavi
from deutschland.abfallnavi.api import fraktionen_api
from deutschland.abfallnavi.model.fraktion import Fraktion
from pprint import pprint
# Defining the host is optional and defaults to https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = abfallnavi.Configuration(
    host = "https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest"
)


# Enter a context with an instance of the API client
with abfallnavi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fraktionen_api.FraktionenApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Müllarten im System
        api_response = api_instance.muellarten()
        pprint(api_response)
    except abfallnavi.ApiException as e:
        print("Exception when calling FraktionenApi->muellarten: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Fraktion]**](Fraktion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **muellarten_pro_hausnummer**
> [Fraktion] muellarten_pro_hausnummer(hausnummern_id)

Müllarten für Hausnummer

Welche Müllarten es an einer Hausnummer gibt. Siehe id unter Pfad `/strassen/{strassenId}` für die hausnummernId.

### Example


```python
import time
from deutschland import abfallnavi
from deutschland.abfallnavi.api import fraktionen_api
from deutschland.abfallnavi.model.fraktion import Fraktion
from pprint import pprint
# Defining the host is optional and defaults to https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = abfallnavi.Configuration(
    host = "https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest"
)


# Enter a context with an instance of the API client
with abfallnavi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fraktionen_api.FraktionenApi(api_client)
    hausnummern_id = 1 # int | Id der Hausnummer

    # example passing only required values which don't have defaults set
    try:
        # Müllarten für Hausnummer
        api_response = api_instance.muellarten_pro_hausnummer(hausnummern_id)
        pprint(api_response)
    except abfallnavi.ApiException as e:
        print("Exception when calling FraktionenApi->muellarten_pro_hausnummer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hausnummern_id** | **int**| Id der Hausnummer |

### Return type

[**[Fraktion]**](Fraktion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **muellarten_pro_strasse**
> [Fraktion] muellarten_pro_strasse(strassen_id)

Müllarten für Straßen

Welche Müllarten es in einer Straße gibt. Siehe id unter Pfad `/orte/{ortId}/strassen` für die strassenId.

### Example


```python
import time
from deutschland import abfallnavi
from deutschland.abfallnavi.api import fraktionen_api
from deutschland.abfallnavi.model.fraktion import Fraktion
from pprint import pprint
# Defining the host is optional and defaults to https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = abfallnavi.Configuration(
    host = "https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest"
)


# Enter a context with an instance of the API client
with abfallnavi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = fraktionen_api.FraktionenApi(api_client)
    strassen_id = 1 # int | Id der Straße

    # example passing only required values which don't have defaults set
    try:
        # Müllarten für Straßen
        api_response = api_instance.muellarten_pro_strasse(strassen_id)
        pprint(api_response)
    except abfallnavi.ApiException as e:
        print("Exception when calling FraktionenApi->muellarten_pro_strasse: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strassen_id** | **int**| Id der Straße |

### Return type

[**[Fraktion]**](Fraktion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

