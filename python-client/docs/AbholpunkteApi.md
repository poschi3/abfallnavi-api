# abfallnavi.AbholpunkteApi

All URIs are relative to *https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hausnummern_pro_strasse**](AbholpunkteApi.md#hausnummern_pro_strasse) | **GET** /strassen/{strassenId} | Hausnummern in Straße
[**ort**](AbholpunkteApi.md#ort) | **GET** /orte/{ortId} | Informationen zu Ort
[**orte**](AbholpunkteApi.md#orte) | **GET** /orte | Orte im System
[**strassen_pro_ort**](AbholpunkteApi.md#strassen_pro_ort) | **GET** /orte/{ortId}/strassen | Straßen im Ort


# **hausnummern_pro_strasse**
> Strasse hausnummern_pro_strasse(strassen_id)

Hausnummern in Straße

Hausnummern in Straße. Siehe id unter Pfad `/orte/{ortId}/strassen` für die strassenId.

### Example


```python
import time
from deutschland import abfallnavi
from deutschland.abfallnavi.api import abholpunkte_api
from deutschland.abfallnavi.model.strasse import Strasse
from pprint import pprint
# Defining the host is optional and defaults to https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = abfallnavi.Configuration(
    host = "https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest"
)


# Enter a context with an instance of the API client
with abfallnavi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = abholpunkte_api.AbholpunkteApi(api_client)
    strassen_id = 1 # int | Id der Straße

    # example passing only required values which don't have defaults set
    try:
        # Hausnummern in Straße
        api_response = api_instance.hausnummern_pro_strasse(strassen_id)
        pprint(api_response)
    except abfallnavi.ApiException as e:
        print("Exception when calling AbholpunkteApi->hausnummern_pro_strasse: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strassen_id** | **int**| Id der Straße |

### Return type

[**Strasse**](Strasse.md)

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

# **ort**
> [Ort2] ort(ort_id)

Informationen zu Ort

Informationen zu einem Ort

### Example


```python
import time
from deutschland import abfallnavi
from deutschland.abfallnavi.api import abholpunkte_api
from deutschland.abfallnavi.model.ort2 import Ort2
from pprint import pprint
# Defining the host is optional and defaults to https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = abfallnavi.Configuration(
    host = "https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest"
)


# Enter a context with an instance of the API client
with abfallnavi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = abholpunkte_api.AbholpunkteApi(api_client)
    ort_id = 1 # int | Id des Ortes

    # example passing only required values which don't have defaults set
    try:
        # Informationen zu Ort
        api_response = api_instance.ort(ort_id)
        pprint(api_response)
    except abfallnavi.ApiException as e:
        print("Exception when calling AbholpunkteApi->ort: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ort_id** | **int**| Id des Ortes |

### Return type

[**[Ort2]**](Ort2.md)

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

# **orte**
> [Ort] orte()

Orte im System

Orte die von diesem API-Endpoint bedient werden.

### Example


```python
import time
from deutschland import abfallnavi
from deutschland.abfallnavi.api import abholpunkte_api
from deutschland.abfallnavi.model.ort import Ort
from pprint import pprint
# Defining the host is optional and defaults to https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = abfallnavi.Configuration(
    host = "https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest"
)


# Enter a context with an instance of the API client
with abfallnavi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = abholpunkte_api.AbholpunkteApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Orte im System
        api_response = api_instance.orte()
        pprint(api_response)
    except abfallnavi.ApiException as e:
        print("Exception when calling AbholpunkteApi->orte: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Ort]**](Ort.md)

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

# **strassen_pro_ort**
> [Strasse] strassen_pro_ort(ort_id)

Straßen im Ort

Straßen im Ort. Siehe id unter Pfad `/orte` für die ortId.  **Warnung**: Die Antwort dieser Anfrage ist zu groß für Anzeige innerhalb der Webseite 

### Example


```python
import time
from deutschland import abfallnavi
from deutschland.abfallnavi.api import abholpunkte_api
from deutschland.abfallnavi.model.strasse import Strasse
from pprint import pprint
# Defining the host is optional and defaults to https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = abfallnavi.Configuration(
    host = "https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest"
)


# Enter a context with an instance of the API client
with abfallnavi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = abholpunkte_api.AbholpunkteApi(api_client)
    ort_id = 1 # int | Id des Ortes

    # example passing only required values which don't have defaults set
    try:
        # Straßen im Ort
        api_response = api_instance.strassen_pro_ort(ort_id)
        pprint(api_response)
    except abfallnavi.ApiException as e:
        print("Exception when calling AbholpunkteApi->strassen_pro_ort: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ort_id** | **int**| Id des Ortes |

### Return type

[**[Strasse]**](Strasse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK  **Hinweis**: Nur für die erste Straße ist &#x60;hausNrList&#x60; befüllt.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

