# abfallnavi.TermineApi

All URIs are relative to *https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_as_file**](TermineApi.md#download_as_file) | **GET** /kalender-{region}/downloadfile.jsp | Datenexport als PDF oder ICS
[**termine_pro_haussnummer**](TermineApi.md#termine_pro_haussnummer) | **GET** /hausnummern/{hausnummernId}/termine | Abholtermine für Hausnummer
[**termine_pro_strasse**](TermineApi.md#termine_pro_strasse) | **GET** /strassen/{strassenId}/termine | Abholtermine für Straße


# **download_as_file**
> str download_as_file(region, format, jahr, ort, strasse, hnr, fraktion)

Datenexport als PDF oder ICS

Datenexport als PDF oder ICS  **Hinweis**: Aus der Webseite heraus kann diese Abfrage nicht ausgeführt werden, weil kein Access-Control-Allow-Origin Header gesetzt wird. 

### Example


```python
import time
from deutschland import abfallnavi
from deutschland.abfallnavi.api import termine_api
from deutschland.abfallnavi.model.region import Region
from pprint import pprint
# Defining the host is optional and defaults to https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = abfallnavi.Configuration(
    host = "https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest"
)


# Enter a context with an instance of the API client
with abfallnavi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = termine_api.TermineApi(api_client)
    region = Region("nuernberg") # Region | Region
    format = "pdf" # str | Datenformat
    jahr = 2022 # int | Jahr
    ort = "Nürnberg" # str | Ortsname
    strasse = 1 # int | Id der Straße
    hnr = 1 # int | Id der Hausnummer
    fraktion = [3,4] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Datenexport als PDF oder ICS
        api_response = api_instance.download_as_file(region, format, jahr, ort, strasse, hnr, fraktion)
        pprint(api_response)
    except abfallnavi.ApiException as e:
        print("Exception when calling TermineApi->download_as_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **Region**| Region |
 **format** | **str**| Datenformat |
 **jahr** | **int**| Jahr |
 **ort** | **str**| Ortsname |
 **strasse** | **int**| Id der Straße |
 **hnr** | **int**| Id der Hausnummer |
 **fraktion** | **[int]**|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **termine_pro_haussnummer**
> [Abholung] termine_pro_haussnummer(hausnummern_id, fraktion)

Abholtermine für Hausnummer

Abholtermine für Hausnummer. Siehe id unter Pfad `/strassen/{strassenId}` für die hausnummernId.

### Example


```python
import time
from deutschland import abfallnavi
from deutschland.abfallnavi.api import termine_api
from deutschland.abfallnavi.model.abholung import Abholung
from pprint import pprint
# Defining the host is optional and defaults to https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = abfallnavi.Configuration(
    host = "https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest"
)


# Enter a context with an instance of the API client
with abfallnavi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = termine_api.TermineApi(api_client)
    hausnummern_id = 1 # int | Id der Hausnummer
    fraktion = [3,4] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Abholtermine für Hausnummer
        api_response = api_instance.termine_pro_haussnummer(hausnummern_id, fraktion)
        pprint(api_response)
    except abfallnavi.ApiException as e:
        print("Exception when calling TermineApi->termine_pro_haussnummer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hausnummern_id** | **int**| Id der Hausnummer |
 **fraktion** | **[int]**|  |

### Return type

[**[Abholung]**](Abholung.md)

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

# **termine_pro_strasse**
> [Abholung] termine_pro_strasse(strassen_id, fraktion)

Abholtermine für Straße

Abholtermine für Straße. Siehe id unter Pfad `/orte/{ortId}/strassen` für die strassenId.

### Example


```python
import time
from deutschland import abfallnavi
from deutschland.abfallnavi.api import termine_api
from deutschland.abfallnavi.model.abholung import Abholung
from pprint import pprint
# Defining the host is optional and defaults to https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = abfallnavi.Configuration(
    host = "https://nuernberg-abfallapp.regioit.de/abfall-app-nuernberg/rest"
)


# Enter a context with an instance of the API client
with abfallnavi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = termine_api.TermineApi(api_client)
    strassen_id = 1 # int | Id der Strasse
    fraktion = [3,4] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        # Abholtermine für Straße
        api_response = api_instance.termine_pro_strasse(strassen_id, fraktion)
        pprint(api_response)
    except abfallnavi.ApiException as e:
        print("Exception when calling TermineApi->termine_pro_strasse: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strassen_id** | **int**| Id der Strasse |
 **fraktion** | **[int]**|  |

### Return type

[**[Abholung]**](Abholung.md)

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

