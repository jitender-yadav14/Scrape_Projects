import requests
import json
import pandas as pd
import time

d1 = list()


class Scraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.agoda.com/en-in/search?city=14552",
            "content-type": "application/json",
            "AG-LANGUAGE-LOCALE": "en-in",
            "ag-debug-override-origin": "IN",
            "AG-REQUEST-ID": "8b374b77-0da5-47d7-94e0-2770d0dfa4be",
            "AG-RETRY-ATTEMPT": "0",
            "AG-REQUEST-ATTEMPT": "1",
            "AG-PAGE-TYPE-ID": "103",
            "AG-CORRELATION-ID": "7ab2b7aa-f432-4869-a553-41435c04b306",
            "AG-ANALYTICS-SESSION-ID": "-148728682283745927",
            "Access-Control-Max-Age": "7200",
            "Origin": "https://www.agoda.com",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
        }

        self.json_data = {
            "operationName": "citySearch",
            "variables": {
                "CitySearchRequest": {
                    "cityId": 14552,
                    "searchRequest": {
                        "searchCriteria": {
                            "isAllowBookOnRequest": True,
                            "bookingDate": "2023-12-20T11:50:03.750Z",
                            "checkInDate": "2023-12-29T11:50:04.057Z",
                            "localCheckInDate": "2023-12-29",
                            "los": 1,
                            "rooms": 1,
                            "adults": 1,
                            "children": 0,
                            "childAges": [],
                            "ratePlans": [],
                            "featureFlagRequest": {
                                "newNumberOfBedroomsConfigFilter": False,
                                "fetchNamesForTealium": True,
                                "fiveStarDealOfTheDay": True,
                                "isAllowBookOnRequest": False,
                                "showUnAvailable": True,
                                "showRemainingProperties": True,
                                "isMultiHotelSearch": False,
                                "enableAgencySupplyForPackages": True,
                                "flags": [
                                    {
                                        "feature": "FamilyChildFriendlyPopularFilter",
                                        "enable": True,
                                    },
                                    {
                                        "feature": "FamilyChildFriendlyPropertyTypeFilter",
                                        "enable": True,
                                    },
                                    {
                                        "feature": "FamilyMode",
                                        "enable": False,
                                    },
                                ],
                                "enablePageToken": True,
                                "enableDealsOfTheDayFilter": False,
                                "isEnableSupplierFinancialInfo": False,
                                "ignoreRequestedNumberOfRoomsForNha": False,
                            },
                            "isUserLoggedIn": False,
                            "currency": "INR",
                            "travellerType": "Couple",
                            "isAPSPeek": False,
                            "enableOpaqueChannel": False,
                            "isEnabledPartnerChannelSelection": None,
                            "sorting": {
                                "sortField": "Ranking",
                                "sortOrder": "Desc",
                                "sortParams": None,
                            },
                            "requiredBasis": "PRPN",
                            "requiredPrice": "Exclusive",
                            "suggestionLimit": 0,
                            "synchronous": False,
                            "supplierPullMetadataRequest": None,
                            "isRoomSuggestionRequested": False,
                            "isAPORequest": False,
                            "hasAPOFilter": False,
                        },
                        "searchContext": {
                            "userId": "ad16d93d-f099-4b1c-8d90-cbc1d7335dc6",
                            "memberId": 0,
                            "locale": "en-in",
                            "cid": 1891461,
                            "origin": "IN",
                            "platform": 1,
                            "deviceTypeId": 1,
                            "experiments": {
                                "forceByVariant": None,
                                "forceByExperiment": [
                                    {
                                        "id": "UMRAH-B2B",
                                        "variant": "B",
                                    },
                                    {
                                        "id": "UMRAH-B2C-REGIONAL",
                                        "variant": "B",
                                    },
                                    {
                                        "id": "UMRAH-B2C",
                                        "variant": "Z",
                                    },
                                    {
                                        "id": "JGCW-204",
                                        "variant": "B",
                                    },
                                ],
                            },
                            "isRetry": False,
                            "showCMS": False,
                            "storeFrontId": 3,
                            "pageTypeId": 103,
                            "whiteLabelKey": None,
                            "ipAddress": "152.58.87.136",
                            "endpointSearchType": "CitySearch",
                            "trackSteps": None,
                            "searchId": "fcb8dc82-ede6-4ba4-8ee3-cf529a1860e2",
                        },
                        "matrix": None,
                        "matrixGroup": [
                            {
                                "matrixGroup": "NumberOfBedrooms",
                                "size": 100,
                            },
                            {
                                "matrixGroup": "LandmarkIds",
                                "size": 10,
                            },
                            {
                                "matrixGroup": "GroupedBedTypes",
                                "size": 100,
                            },
                            {
                                "matrixGroup": "RoomBenefits",
                                "size": 100,
                            },
                            {
                                "matrixGroup": "AtmosphereIds",
                                "size": 100,
                            },
                            {
                                "matrixGroup": "RoomAmenities",
                                "size": 100,
                            },
                            {
                                "matrixGroup": "AffordableCategory",
                                "size": 100,
                            },
                            {
                                "matrixGroup": "HotelFacilities",
                                "size": 100,
                            },
                            {
                                "matrixGroup": "BeachAccessTypeIds",
                                "size": 100,
                            },
                            {
                                "matrixGroup": "StarRating",
                                "size": 20,
                            },
                            {
                                "matrixGroup": "AllGuestReviewBreakdown",
                                "size": 100,
                            },
                            {
                                "matrixGroup": "MetroSubwayStationLandmarkIds",
                                "size": 20,
                            },
                            {
                                "matrixGroup": "CityCenterDistance",
                                "size": 100,
                            },
                            {
                                "matrixGroup": "ProductType",
                                "size": 100,
                            },
                            {
                                "matrixGroup": "TripPurpose",
                                "size": 5,
                            },
                            {
                                "matrixGroup": "BusStationLandmarkIds",
                                "size": 20,
                            },
                            {
                                "matrixGroup": "IsSustainableTravel",
                                "size": 2,
                            },
                            {
                                "matrixGroup": "ReviewLocationScore",
                                "size": 3,
                            },
                            {
                                "matrixGroup": "LandmarkSubTypeCategoryIds",
                                "size": 20,
                            },
                            {
                                "matrixGroup": "ReviewScore",
                                "size": 100,
                            },
                            {
                                "matrixGroup": "AccommodationType",
                                "size": 100,
                            },
                            {
                                "matrixGroup": "PaymentOptions",
                                "size": 100,
                            },
                            {
                                "matrixGroup": "TrainStationLandmarkIds",
                                "size": 20,
                            },
                            {
                                "matrixGroup": "HotelAreaId",
                                "size": 100,
                            },
                            {
                                "matrixGroup": "HotelChainId",
                                "size": 10,
                            },
                            {
                                "matrixGroup": "RecommendedByDestinationCity",
                                "size": 10,
                            },
                            {
                                "matrixGroup": "Deals",
                                "size": 100,
                            },
                        ],
                        "filterRequest": {
                            "idsFilters": [],
                            "rangeFilters": [],
                            "textFilters": [],
                        },
                        "page": {
                            "pageSize": 45,
                            "pageNumber": 1,
                            "pageToken": "AEsQBCAUSvwEKvAGYka0WvJzbE56k2xaT3aUWid2FEZyvmQTyyf0R/dUC3YqeEc2XbpaDTs7EgRSf9z6Mr8AWjocS3JXQFoLK/QO+/QSnnsgRju+HEbO0uBLqit4Rk+K3DOyH7BH/yRCfq8gLmcCJD9ycnAX6yw+7uZMRm7zLEvixC+efnAXq1vMOu0DZ6UDmhBP1ocYImqWNFJCuEsbtOOKPEZmb+BCh94ITzJ7lA4Ol5QOgkRHv+xeb/SvUmRGn944M6umzAhK4AQgBErMBCrAB3O2dEc3C2xGU7/EVntvLFoGKCemcG6iQhxKAuJwFqLnnBY/VEq3Asguz9o0B9Py4A77MIsGWiA7P2ZsBy8jaAabvHcKJug3kpucRiPAJh9GmAcGptwzLlxy39j/s0fER/sERjrciwpmDBZWDCvWpgA/B1/AIqM2HBZn5pgvflA+35KcCrNkvgYcunq8LzZwEpLIh8YCDE4u3sxDsyyKWjwvhlA+ZiaMFqfaxAb7/mQESuQEIBhK0AQqxAdCSrRayhpkSqLLZE8nP+g741ZkVhJ3QFuPbuQyF9bgD2M46mcSYEMLvLOePD+XDwhC0tIMRzY3QFqDtjhCrsZkF1JLxCNvHkhbA+6MFx4ncFrP/ghP7/MIN+froBMj6F82d5QPKuo8IubQY4/TcDf2L2xPi4O8Rz8ERjPLPEdG/gxKKzoETptnNDt3iEZOrEJ7FzAu/nvwS99vNDfnj0BO2rBCG0ocP9JUO5KEhqam8ARLHAQgCEsIBCr8BzrSGA82YsxW/+qMUysW9FveW8Qi9mLsCwvXRFcXXsxXh7KsIyp6cBb3AnwHFthiD+JQVx5umFuvREICQhA+Pkw+30c0OzKCBD7GZ5ALZr/AV9vMXx8oQ/p2KAdWohwXjkLMT2fKmBaWBD7T5kBTo2Qap2Qa4thjvy5cO16m0FY0ml4w1xuHTBObaCdyk7xP2jQ+Lhxi++8wK7oQbpLWGA+r48BHtpv4KroafE7aFtw3Ty/MOxaXNEYSE2QSDmBwSxwEIAxLCAQq/Af6H0BWt0tEVu+6REq/7khT2oRvijNUEtPupEIu/EYn1uAOThN0QhoTkEY6YnhHps+YIy5wEufuBCdrVghDEtKoEhOsRp4kQ4ZSECeqk4w/T9uIOgaMMi+yIEq+StgGiyHf62gm89NoOnsn1DrSh0xXq7sIV/MrMEpP28BGY14kVqIq6DbDkswLD1JoRp4SGErig8Bax4oUBxarnFruOqAuelUeflYMDwO/0Cs2Kug387/4V3ITzFcq+kRCBipcMErkBCAQStAEKsQHyrPoF1Me9FomQ0Ba60w/asNUTwZwd1p6CEM2enAX/1QKwthHS2YAB/L8g/orQFaui7AWlnZwF640Sm7CGA8/a/g7t9IITsa2GA9usEIe1mBDl054Bq0Kr29MU/d2kEaXZBqz/BI3ovRTOncEEwcAPn8K9FuHWgQjHtdAW6ZcRmZ66EqPLwAm9qcgLzb7CFcmT0BaTp/sKmJED2tnPAoDwrxHk/xqgu60MhdqBFaequwQaBAgFEDEaBAgBEDEaBAgGEDEaBAgCEDEaBAgDEDEaBAgEEDE=",
                        },
                        "apoRequest": {
                            "apoPageSize": 10,
                        },
                        "searchHistory": [
                            {
                                "objectId": 407262,
                                "searchDate": "2023-12-19",
                                "searchType": "PropertySearch",
                                "childrenAges": [],
                            },
                            {
                                "objectId": 148737,
                                "searchDate": "2023-12-20",
                                "searchType": "PropertySearch",
                                "childrenAges": [],
                            },
                        ],
                        "searchDetailRequest": {
                            "priceHistogramBins": 50,
                        },
                        "isTrimmedResponseRequested": False,
                        "featuredAgodaHomesRequest": None,
                        "featuredLuxuryHotelsRequest": None,
                        "highlyRatedAgodaHomesRequest": {
                            "numberOfAgodaHomes": 30,
                            "minimumReviewScore": 7.5,
                            "minimumReviewCount": 3,
                            "accommodationTypes": [
                                28,
                                29,
                                30,
                                102,
                                103,
                                106,
                                107,
                                108,
                                109,
                                110,
                                114,
                                115,
                                120,
                                131,
                            ],
                            "sortVersion": 0,
                        },
                        "extraAgodaHomesRequest": None,
                        "extraHotels": {
                            "extraHotelIds": [],
                            "enableFiltersForExtraHotels": False,
                        },
                        "packaging": None,
                        "flexibleSearchRequest": {
                            "fromDate": "2023-12-20",
                            "toDate": "2024-01-28",
                            "alternativeDateSize": 4,
                            "isFullFlexibleDateSearch": False,
                        },
                        "rankingRequest": {
                            "isNhaKeywordSearch": False,
                        },
                        "rocketmilesRequestV2": None,
                        "featuredPulsePropertiesRequest": {
                            "numberOfPulseProperties": 15,
                        },
                    },
                },
                "ContentSummaryRequest": {
                    "context": {
                        "rawUserId": "ad16d93d-f099-4b1c-8d90-cbc1d7335dc6",
                        "memberId": 0,
                        "userOrigin": "IN",
                        "locale": "en-in",
                        "forceExperimentsByIdNew": [
                            {
                                "key": "UMRAH-B2B",
                                "value": "B",
                            },
                            {
                                "key": "UMRAH-B2C-REGIONAL",
                                "value": "B",
                            },
                            {
                                "key": "UMRAH-B2C",
                                "value": "Z",
                            },
                            {
                                "key": "JGCW-204",
                                "value": "B",
                            },
                        ],
                        "apo": False,
                        "searchCriteria": {
                            "cityId": 14552,
                        },
                        "platform": {
                            "id": 1,
                        },
                        "storeFrontId": 3,
                        "cid": "1891461",
                        "occupancy": {
                            "numberOfAdults": 1,
                            "numberOfChildren": 0,
                            "travelerType": 0,
                            "checkIn": "2023-12-29T11:50:04.057Z",
                        },
                        "deviceTypeId": 1,
                        "whiteLabelKey": "",
                        "correlationId": "",
                    },
                    "summary": {
                        "highlightedFeaturesOrderPriority": None,
                        "includeHotelCharacter": True,
                    },
                    "reviews": {
                        "commentary": None,
                        "demographics": {
                            "providerIds": None,
                            "filter": {
                                "defaultProviderOnly": True,
                            },
                        },
                        "summaries": {
                            "providerIds": None,
                            "apo": True,
                            "limit": 1,
                            "travellerType": 0,
                        },
                        "cumulative": {
                            "providerIds": None,
                        },
                        "filters": None,
                    },
                    "images": {
                        "page": None,
                        "maxWidth": 0,
                        "maxHeight": 0,
                        "imageSizes": None,
                        "indexOffset": None,
                    },
                    "rooms": {
                        "images": None,
                        "featureLimit": 0,
                        "filterCriteria": None,
                        "includeMissing": False,
                        "includeSoldOut": False,
                        "includeDmcRoomId": False,
                        "soldOutRoomCriteria": None,
                        "showRoomSize": True,
                        "showRoomFacilities": True,
                        "showRoomName": False,
                    },
                    "nonHotelAccommodation": True,
                    "engagement": True,
                    "highlights": {
                        "maxNumberOfItems": 0,
                        "images": {
                            "imageSizes": [
                                {
                                    "key": "full",
                                    "size": {
                                        "width": 0,
                                        "height": 0,
                                    },
                                },
                            ],
                        },
                    },
                    "personalizedInformation": False,
                    "localInformation": {
                        "images": None,
                    },
                    "features": None,
                    "rateCategories": True,
                    "contentRateCategories": {
                        "escapeRateCategories": {},
                    },
                    "synopsis": True,
                },
                "PricingSummaryRequest": {
                    "cheapestOnly": True,
                    "context": {
                        "isAllowBookOnRequest": True,
                        "abTests": [
                            {
                                "testId": 9021,
                                "abUser": "B",
                            },
                            {
                                "testId": 9023,
                                "abUser": "B",
                            },
                            {
                                "testId": 9024,
                                "abUser": "B",
                            },
                            {
                                "testId": 9025,
                                "abUser": "B",
                            },
                            {
                                "testId": 9027,
                                "abUser": "B",
                            },
                            {
                                "testId": 9029,
                                "abUser": "B",
                            },
                        ],
                        "clientInfo": {
                            "cid": 1891461,
                            "languageId": 1,
                            "languageUse": 1,
                            "origin": "IN",
                            "platform": 1,
                            "searchId": "fcb8dc82-ede6-4ba4-8ee3-cf529a1860e2",
                            "storefront": 3,
                            "userId": "ad16d93d-f099-4b1c-8d90-cbc1d7335dc6",
                            "ipAddress": "152.58.87.136",
                        },
                        "experiment": [
                            {
                                "name": "UMRAH-B2B",
                                "variant": "B",
                            },
                            {
                                "name": "UMRAH-B2C-REGIONAL",
                                "variant": "B",
                            },
                            {
                                "name": "UMRAH-B2C",
                                "variant": "Z",
                            },
                            {
                                "name": "JGCW-204",
                                "variant": "B",
                            },
                        ],
                        "sessionInfo": {
                            "isLogin": False,
                            "memberId": 0,
                            "sessionId": 1,
                        },
                        "packaging": None,
                    },
                    "isSSR": True,
                    "pricing": {
                        "bookingDate": "2023-12-20T11:50:03.739Z",
                        "checkIn": "2023-12-29T11:50:04.057Z",
                        "checkout": "2023-12-30T11:50:04.057Z",
                        "localCheckInDate": "2023-12-29",
                        "localCheckoutDate": "2023-12-30",
                        "currency": "INR",
                        "details": {
                            "cheapestPriceOnly": False,
                            "itemBreakdown": False,
                            "priceBreakdown": False,
                        },
                        "featureFlag": [
                            "ClientDiscount",
                            "PriceHistory",
                            "VipPlatinum",
                            "RatePlanPromosCumulative",
                            "PromosCumulative",
                            "CouponSellEx",
                            "MixAndSave",
                            "APSPeek",
                            "StackChannelDiscount",
                            "AutoApplyPromos",
                            "EnableAgencySupplyForPackages",
                            "EnableCashback",
                            "CreditCardPromotionPeek",
                            "EnableCofundedCashback",
                            "DispatchGoLocalForInternational",
                            "EnableGoToTravelCampaign",
                            "EnablePriceTrend",
                        ],
                        "features": {
                            "crossOutRate": False,
                            "isAPSPeek": False,
                            "isAllOcc": False,
                            "isApsEnabled": False,
                            "isIncludeUsdAndLocalCurrency": False,
                            "isMSE": True,
                            "isRPM2Included": True,
                            "maxSuggestions": 0,
                            "isEnableSupplierFinancialInfo": False,
                            "isLoggingAuctionData": False,
                            "newRateModel": False,
                            "overrideOccupancy": False,
                            "filterCheapestRoomEscapesPackage": False,
                            "priusId": 0,
                            "synchronous": False,
                            "enableRichContentOffer": True,
                            "showCouponAmountInUserCurrency": False,
                            "disableEscapesPackage": False,
                            "enablePushDayUseRates": False,
                            "enableDayUseCor": False,
                        },
                        "filters": {
                            "cheapestRoomFilters": [],
                            "filterAPO": False,
                            "ratePlans": [
                                1,
                            ],
                            "secretDealOnly": False,
                            "suppliers": [],
                            "nosOfBedrooms": [],
                        },
                        "includedPriceInfo": False,
                        "occupancy": {
                            "adults": 1,
                            "children": 0,
                            "childAges": [],
                            "rooms": 1,
                            "childrenTypes": [],
                        },
                        "supplierPullMetadata": {
                            "requiredPrecheckAccuracyLevel": 0,
                        },
                        "mseHotelIds": [],
                        "ppLandingHotelIds": [],
                        "searchedHotelIds": [],
                        "paymentId": -1,
                        "externalLoyaltyRequest": None,
                    },
                    "suggestedPrice": "Exclusive",
                },
                "PriceStreamMetaLabRequest": {
                    "attributesId": [
                        8,
                        1,
                        18,
                        7,
                        11,
                        2,
                        3,
                    ],
                },
            },
            "query": "query citySearch($CitySearchRequest: CitySearchRequest!, $ContentSummaryRequest: ContentSummaryRequest!, $PricingSummaryRequest: PricingRequestParameters, $PriceStreamMetaLabRequest: PriceStreamMetaLabRequest) {\n  citySearch(CitySearchRequest: $CitySearchRequest) {\n    featuredPulseProperties(ContentSummaryRequest: $ContentSummaryRequest, PricingSummaryRequest: $PricingSummaryRequest) {\n      propertyId\n      propertyResultType\n      pricing {\n        pulseCampaignMetadata {\n          promotionTypeId\n          webCampaignId\n          campaignTypeId\n          campaignBadgeText\n          campaignBadgeDescText\n          dealExpiryTime\n          showPulseMerchandise\n        }\n        isAvailable\n        isReady\n        offers {\n          roomOffers {\n            room {\n              pricing {\n                currency\n                price {\n                  perNight {\n                    exclusive {\n                      crossedOutPrice\n                      display\n                    }\n                    inclusive {\n                      crossedOutPrice\n                      display\n                    }\n                  }\n                  perRoomPerNight {\n                    exclusive {\n                      crossedOutPrice\n                      display\n                    }\n                    inclusive {\n                      crossedOutPrice\n                      display\n                    }\n                  }\n                }\n              }\n            }\n          }\n        }\n      }\n      content {\n        reviews {\n          contentReview {\n            isDefault\n            providerId\n            cumulative {\n              reviewCount\n              score\n            }\n          }\n          cumulative {\n            reviewCount\n            score\n          }\n        }\n        images {\n          hotelImages {\n            urls {\n              value\n            }\n          }\n        }\n        informationSummary {\n          hasHostExperience\n          displayName\n          rating\n          propertyLinks {\n            propertyPage\n          }\n          address {\n            country {\n              id\n            }\n            area {\n              name\n            }\n            city {\n              name\n            }\n          }\n          nhaSummary {\n            hostType\n          }\n        }\n      }\n    }\n    searchResult {\n      sortMatrix {\n        result {\n          fieldId\n          sorting {\n            sortField\n            sortOrder\n            sortParams {\n              id\n            }\n          }\n          display {\n            name\n          }\n          childMatrix {\n            fieldId\n            sorting {\n              sortField\n              sortOrder\n              sortParams {\n                id\n              }\n            }\n            display {\n              name\n            }\n            childMatrix {\n              fieldId\n              sorting {\n                sortField\n                sortOrder\n                sortParams {\n                  id\n                }\n              }\n              display {\n                name\n              }\n            }\n          }\n        }\n      }\n      searchInfo {\n        flexibleSearch {\n          currentDate {\n            checkIn\n            price\n          }\n          alternativeDates {\n            checkIn\n            price\n          }\n        }\n        hasSecretDeal\n        isComplete\n        totalFilteredHotels\n        hasEscapesPackage\n        searchStatus {\n          searchCriteria {\n            checkIn\n          }\n          searchStatus\n        }\n        objectInfo {\n          objectName\n          cityName\n          cityEnglishName\n          countryId\n          countryEnglishName\n          mapLatitude\n          mapLongitude\n          mapZoomLevel\n          wlPreferredCityName\n          wlPreferredCountryName\n          cityId\n          cityCenterPolygon {\n            geoPoints {\n              lon\n              lat\n            }\n            touristAreaCenterPoint {\n              lon\n              lat\n            }\n          }\n        }\n      }\n      urgencyDetail {\n        urgencyScore\n      }\n      histogram {\n        bins {\n          numOfElements\n          upperBound {\n            perNightPerRoom\n            perPax\n          }\n        }\n      }\n      nhaProbability\n    }\n    properties(ContentSummaryRequest: $ContentSummaryRequest, PricingSummaryRequest: $PricingSummaryRequest, PriceStreamMetaLabRequest: $PriceStreamMetaLabRequest) {\n      propertyId\n      sponsoredDetail {\n        sponsoredType\n        trackingData\n        isShowSponsoredFlag\n      }\n      propertyResultType\n      content {\n        informationSummary {\n          hotelCharacter {\n            hotelTag {\n              name\n              symbol\n            }\n            hotelView {\n              name\n              symbol\n            }\n          }\n          propertyLinks {\n            propertyPage\n          }\n          atmospheres {\n            id\n            name\n          }\n          isSustainableTravel\n          localeName\n          defaultName\n          displayName\n          accommodationType\n          awardYear\n          hasHostExperience\n          nhaSummary {\n            hostPropertyCount\n          }\n          address {\n            countryCode\n            country {\n              id\n              name\n            }\n            city {\n              id\n              name\n            }\n            area {\n              id\n              name\n            }\n          }\n          propertyType\n          rating\n          agodaGuaranteeProgram\n          remarks {\n            renovationInfo {\n              renovationType\n              year\n            }\n          }\n          spokenLanguages {\n            id\n          }\n          geoInfo {\n            latitude\n            longitude\n          }\n        }\n        propertyEngagement {\n          lastBooking\n          peopleLooking\n        }\n        nonHotelAccommodation {\n          masterRooms {\n            noOfBathrooms\n            noOfBedrooms\n            noOfBeds\n            roomSizeSqm\n            highlightedFacilities\n          }\n          hostLevel {\n            id\n            name\n          }\n          supportedLongStay\n        }\n        facilities {\n          id\n        }\n        images {\n          hotelImages {\n            id\n            caption\n            providerId\n            urls {\n              key\n              value\n            }\n          }\n        }\n        reviews {\n          contentReview {\n            isDefault\n            providerId\n            demographics {\n              groups {\n                id\n                grades {\n                  id\n                  score\n                }\n              }\n            }\n            summaries {\n              recommendationScores {\n                recommendationScore\n              }\n              snippets {\n                countryId\n                countryCode\n                countryName\n                date\n                demographicId\n                demographicName\n                reviewer\n                reviewRating\n                snippet\n              }\n            }\n            cumulative {\n              reviewCount\n              score\n            }\n          }\n          cumulative {\n            reviewCount\n            score\n          }\n          cumulativeForHost {\n            hostAvgHotelReviewRating\n            hostHotelReviewTotalCount\n          }\n        }\n        familyFeatures {\n          hasChildrenFreePolicy\n          isFamilyRoom\n          hasMoreThanOneBedroom\n          isInterConnectingRoom\n          isInfantCottageAvailable\n          hasKidsPool\n          hasKidsClub\n        }\n        personalizedInformation {\n          childrenFreePolicy {\n            fromAge\n            toAge\n          }\n        }\n        localInformation {\n          landmarks {\n            transportation {\n              landmarkName\n              distanceInM\n            }\n            topLandmark {\n              landmarkName\n              distanceInM\n            }\n            beach {\n              landmarkName\n              distanceInM\n            }\n          }\n          hasAirportTransfer\n        }\n        highlight {\n          cityCenter {\n            distanceFromCityCenter\n          }\n          favoriteFeatures {\n            features {\n              id\n              title\n              category\n            }\n          }\n          hasNearbyPublicTransportation\n        }\n        rateCategories {\n          escapeRateCategories {\n            rateCategoryId\n            localizedRateCategoryName\n          }\n        }\n      }\n      soldOut {\n        soldOutPrice {\n          averagePrice\n        }\n      }\n      pricing {\n        pulseCampaignMetadata {\n          promotionTypeId\n          webCampaignId\n          campaignTypeId\n          campaignBadgeText\n          campaignBadgeDescText\n          dealExpiryTime\n          showPulseMerchandise\n        }\n        isAvailable\n        isReady\n        benefits\n        cheapestRoomOffer {\n          agodaCash {\n            showBadge\n            giftcardGuid\n            dayToEarn\n            earnId\n            percentage\n            expiryDay\n          }\n          cashback {\n            cashbackGuid\n            showPostCashbackPrice\n            cashbackVersion\n            percentage\n            earnId\n            dayToEarn\n            expiryDay\n            cashbackType\n            appliedCampaignName\n          }\n        }\n        isEasyCancel\n        isInsiderDeal\n        suggestPriceType {\n          suggestPrice\n        }\n        roomBundle {\n          bundleId\n          bundleType\n          saveAmount {\n            perNight {\n              ...Fragaif92hhgg99cfeabgb19\n            }\n          }\n        }\n        pointmax {\n          channelId\n          point\n        }\n        priceChange {\n          changePercentage\n          searchDate\n        }\n        payment {\n          cancellation {\n            cancellationType\n            freeCancellationDate\n          }\n          payLater {\n            isEligible\n          }\n          payAtHotel {\n            isEligible\n          }\n          noCreditCard {\n            isEligible\n          }\n          taxReceipt {\n            isEligible\n          }\n        }\n        cheapestStayPackageRatePlans {\n          stayPackageType\n          ratePlanId\n        }\n        pricingMessages {\n          location\n          ids\n        }\n        suppliersSummaries {\n          id\n          supplierHotelId\n        }\n        supplierInfo {\n          id\n          name\n          isAgodaBand\n        }\n        offers {\n          roomOffers {\n            room {\n              extraPriceInfo {\n                displayPriceWithSurchargesPRPN\n                corDisplayPriceWithSurchargesPRPN\n              }\n              availableRooms\n              isPromoEligible\n              promotions {\n                typeId\n                promotionDiscount {\n                  value\n                }\n                isRatePlanAsPromotion\n                cmsTypeId\n                description\n              }\n              bookingDuration {\n                unit\n                value\n              }\n              supplierId\n              corSummary {\n                hasCor\n                corType\n                isOriginal\n                hasOwnCOR\n                isBlacklistedCor\n              }\n              localVoucher {\n                currencyCode\n                amount\n              }\n              pricing {\n                currency\n                price {\n                  perNight {\n                    exclusive {\n                      display\n                      cashbackPrice\n                      displayAfterCashback\n                      originalPrice\n                    }\n                    inclusive {\n                      display\n                      cashbackPrice\n                      displayAfterCashback\n                      originalPrice\n                    }\n                  }\n                  perBook {\n                    exclusive {\n                      display\n                      cashbackPrice\n                      displayAfterCashback\n                      rebatePrice\n                      originalPrice\n                      autoAppliedPromoDiscount\n                    }\n                    inclusive {\n                      display\n                      cashbackPrice\n                      displayAfterCashback\n                      rebatePrice\n                      originalPrice\n                      autoAppliedPromoDiscount\n                    }\n                  }\n                  perRoomPerNight {\n                    exclusive {\n                      display\n                      crossedOutPrice\n                      cashbackPrice\n                      displayAfterCashback\n                      rebatePrice\n                      pseudoCouponPrice\n                      originalPrice\n                      loyaltyOfferSummary {\n                        basePrice {\n                          exclusive\n                          allInclusive\n                        }\n                        offers {\n                          identifier\n                          burn {\n                            points\n                            payableAmount\n                          }\n                          earn {\n                            points\n                          }\n                          offerType\n                          isSelected\n                        }\n                      }\n                    }\n                    inclusive {\n                      display\n                      crossedOutPrice\n                      cashbackPrice\n                      displayAfterCashback\n                      rebatePrice\n                      pseudoCouponPrice\n                      originalPrice\n                      loyaltyOfferSummary {\n                        basePrice {\n                          exclusive\n                          allInclusive\n                        }\n                        offers {\n                          identifier\n                          burn {\n                            points\n                            payableAmount\n                          }\n                          earn {\n                            points\n                          }\n                          offerType\n                          isSelected\n                        }\n                      }\n                    }\n                  }\n                  totalDiscount\n                  priceAfterAppliedAgodaCash {\n                    perBook {\n                      ...Fraga1j4f6848fdfa7e82cie\n                    }\n                    perRoomPerNight {\n                      ...Fraga1j4f6848fdfa7e82cie\n                    }\n                  }\n                }\n                apsPeek {\n                  perRoomPerNight {\n                    ...Fragaif92hhgg99cfeabgb19\n                  }\n                }\n                promotionPricePeek {\n                  display {\n                    perBook {\n                      ...Fragaif92hhgg99cfeabgb19\n                    }\n                    perRoomPerNight {\n                      ...Fragaif92hhgg99cfeabgb19\n                    }\n                    perNight {\n                      ...Fragaif92hhgg99cfeabgb19\n                    }\n                  }\n                  discountType\n                  promotionCodeType\n                  promotionCode\n                  promoAppliedOnFinalPrice\n                  childPromotions {\n                    campaignId\n                  }\n                  campaignName\n                }\n                channelDiscountSummary {\n                  channelDiscountBreakdown {\n                    display\n                    discountPercent\n                    channelId\n                  }\n                }\n                promotionsCumulative {\n                  promotionCumulativeType\n                  amountPercentage\n                  minNightsStay\n                }\n              }\n              uid\n              payment {\n                cancellation {\n                  cancellationType\n                }\n              }\n              discount {\n                deals\n                channelDiscount\n              }\n              saveUpTo {\n                perRoomPerNight\n              }\n              benefits {\n                id\n                targetType\n              }\n              channel {\n                id\n              }\n              mseRoomSummaries {\n                supplierId\n                subSupplierId\n                pricingSummaries {\n                  currency\n                  channelDiscountSummary {\n                    channelDiscountBreakdown {\n                      channelId\n                      discountPercent\n                      display\n                    }\n                  }\n                  price {\n                    perRoomPerNight {\n                      exclusive {\n                        display\n                      }\n                      inclusive {\n                        display\n                      }\n                    }\n                  }\n                }\n              }\n              cashback {\n                cashbackGuid\n                showPostCashbackPrice\n                cashbackVersion\n                percentage\n                earnId\n                dayToEarn\n                expiryDay\n                cashbackType\n                appliedCampaignName\n              }\n              agodaCash {\n                showBadge\n                giftcardGuid\n                dayToEarn\n                expiryDay\n                percentage\n              }\n              corInfo {\n                corBreakdown {\n                  taxExPN {\n                    ...Fragj2f1ab8ffh74319d35c1\n                  }\n                  taxInPN {\n                    ...Fragj2f1ab8ffh74319d35c1\n                  }\n                  taxExPRPN {\n                    ...Fragj2f1ab8ffh74319d35c1\n                  }\n                  taxInPRPN {\n                    ...Fragj2f1ab8ffh74319d35c1\n                  }\n                }\n                corInfo {\n                  corType\n                }\n              }\n              loyaltyDisplay {\n                items\n              }\n              capacity {\n                extraBedsAvailable\n              }\n              pricingMessages {\n                formatted {\n                  location\n                  texts {\n                    index\n                    text\n                  }\n                }\n              }\n              campaign {\n                selected {\n                  campaignId\n                  promotionId\n                  messages {\n                    campaignName\n                    title\n                    titleWithDiscount\n                    description\n                    linkOutText\n                    url\n                  }\n                }\n              }\n              stayPackageType\n            }\n          }\n        }\n      }\n      metaLab {\n        attributes {\n          attributeId\n          dataType\n          value\n          version\n        }\n      }\n      enrichment {\n        topSellingPoint {\n          tspType\n          value\n        }\n        pricingBadges {\n          badges\n        }\n        uniqueSellingPoint {\n          rank\n          segment\n          uspType\n          uspPropertyType\n        }\n        bookingHistory {\n          bookingCount {\n            count\n            timeFrame\n          }\n        }\n        showReviewSnippet\n        isPopular\n        roomInformation {\n          cheapestRoomSizeSqm\n          facilities {\n            id\n            propertyFacilityName\n            symbol\n          }\n        }\n      }\n    }\n    searchEnrichment {\n      suppliersInformation {\n        supplierId\n        supplierName\n        isAgodaBand\n      }\n      pageToken\n    }\n    aggregation {\n      matrixGroupResults {\n        matrixGroup\n        matrixItemResults {\n          id\n          name\n          count\n          filterKey\n          filterRequestType\n          extraDataResults {\n            text\n            matrixExtraDataType\n          }\n        }\n      }\n    }\n  }\n}\n\nfragment Fraga1j4f6848fdfa7e82cie on DisplayPrice {\n  exclusive\n  allInclusive\n}\n\nfragment Fragaif92hhgg99cfeabgb19 on DFDisplayPrice {\n  exclusive\n  allInclusive\n}\n\nfragment Fragj2f1ab8ffh74319d35c1 on DFCorBreakdownItem {\n  price\n  id\n}\n",
        }

        self.json_detail_page = {
            "operationName": "propertyDetailsSearch",
            "variables": {
                "PropertyDetailsRequest": {
                    "propertyIds": [],
                },
                "ContentImagesRequest": {
                    "imageSizes": [
                        {
                            "key": "main",
                            "size": {
                                "width": 1024,
                                "height": 768,
                            },
                        },
                        {
                            "key": "gallery_preview",
                            "size": {
                                "width": 450,
                                "height": 450,
                            },
                        },
                        {
                            "key": "thumbnail",
                            "size": {
                                "width": 80,
                                "height": 60,
                            },
                        },
                        {
                            "key": "thumbnail-2x",
                            "size": {
                                "width": 160,
                                "height": 120,
                            },
                        },
                    ],
                    "isApo": False,
                    "isUseNewImageCaption": True,
                },
                "ContentReviewSummariesRequest": {
                    "providerIds": [
                        332,
                        3038,
                        27901,
                        28999,
                        29100,
                        27999,
                        27980,
                        27989,
                        29014,
                    ],
                    "occupancyRequest": {
                        "numberOfAdults": 1,
                        "numberOfChildren": 0,
                        "travelerType": 0,
                        "lengthOfStay": 1,
                        "checkIn": "2023-12-28T18:30:00.000Z",
                    },
                    "contentReviewPositiveMentionsRequest": {
                        "facilityClassesLimit": 3,
                        "facilityClassesSentimentLimit": 3,
                    },
                    "contentReviewSnippetsRequest": {
                        "overrideLimit": 20,
                    },
                    "isApo": False,
                },
                "ContentReviewScoreRequest": {
                    "demographics": {
                        "filter": {
                            "defaultProviderOnly": True,
                        },
                    },
                    "providerIds": [],
                },
                "ContentInformationSummaryRequest": {
                    "isApo": False,
                },
                "ContentHighlightsRequest": {
                    "includeAtfPropertyHighlights": True,
                    "maxNumberOfItems": 5,
                    "occupancyRequest": {
                        "numberOfAdults": 1,
                        "numberOfChildren": 0,
                        "travelerType": 3,
                    },
                    "images": {
                        "imageSizes": [
                            {
                                "key": "main",
                                "size": {
                                    "width": 360,
                                    "height": 270,
                                },
                            },
                        ],
                    },
                },
                "ContentLocalInformationRequest": {
                    "showWalkablePlaces": True,
                    "images": {
                        "imageSizes": [
                            {
                                "key": "main",
                                "size": {
                                    "width": 360,
                                    "height": 270,
                                },
                            },
                        ],
                    },
                },
                "ContentInformationRequest": {
                    "isApo": False,
                    "characteristicTopicsLimit": 3,
                    "showDynamicShortDescription": True,
                },
                "ContentFeaturesRequest": {
                    "includeFacilityHighlights": True,
                    "occupancyRequest": {
                        "numberOfAdults": 1,
                        "numberOfChildren": 0,
                        "travelerType": 0,
                        "lengthOfStay": 1,
                    },
                    "images": {
                        "imageSizes": [
                            {
                                "key": "original",
                                "size": {
                                    "width": 360,
                                    "height": 270,
                                },
                            },
                        ],
                    },
                },
                "PriceStreamMetaLabRequest": {
                    "attributesId": [
                        8,
                        2,
                        3,
                        7,
                        18,
                    ],
                },
            },
            "query": "query propertyDetailsSearch($PropertyDetailsRequest: PropertyDetailsRequest!, $ContentImagesRequest: ContentImagesRequest!, $ContentReviewSummariesRequest: ContentReviewSummariesRequest, $ContentReviewScoreRequest: ContentReviewScoreRequest, $ContentInformationSummaryRequest: ContentInformationSummaryRequest, $ContentHighlightsRequest: ContentHighlightsRequest, $ContentLocalInformationRequest: ContentLocalInformationRequest, $ContentInformationRequest: ContentInformationRequest, $ContentFeaturesRequest: ContentFeaturesRequest, $PriceStreamMetaLabRequest: PriceStreamMetaLabRequest!) {\n  propertyDetailsSearch(PropertyDetailsRequest: $PropertyDetailsRequest) {\n    propertyDetails {\n      propertyId\n      propertyMetaInfo {\n        propertyMetaRanking {\n          numberOfProperty\n          metrics {\n            metricName\n            rank\n            absoluteValue\n          }\n        }\n      }\n      contentDetail {\n        propertyId\n        contentImages(ContentImagesRequest: $ContentImagesRequest) {\n          hotelImages {\n            caption\n            groupEntityId\n            groupId\n            id\n            providerId\n            typeId\n            uploadedDate\n            highResolutionSizes\n            urls {\n              key\n              value\n            }\n          }\n          videos {\n            id\n            location\n          }\n          matterports {\n            id\n            orderId\n            roomTypeId\n            thumbnailUrl\n            url\n          }\n        }\n        contentReviewSummaries(ContentReviewSummariesRequest: $ContentReviewSummariesRequest) {\n          snippets {\n            snippetId\n            countryCode\n            countryId\n            countryName\n            date\n            demographicId\n            demographicName\n            reviewer\n            reviewRating\n            snippet\n            topics {\n              score\n              topicId\n            }\n          }\n          recommendationScores {\n            frequentTravellerRecommendationScore\n            recommendationScore\n          }\n          positiveMentions {\n            categories {\n              id\n              name\n              score\n            }\n            facilityClassesSentiment {\n              facilityIds\n              id\n              name\n              noOfPositiveMentioned\n            }\n            facilityClasses {\n              facilityIds\n              id\n              name\n              noOfMentioned\n            }\n          }\n        }\n        contentReviewScore(ContentReviewScoreRequest: $ContentReviewScoreRequest) {\n          combinedReviewScore {\n            cumulative {\n              maxScore\n              reviewCount\n              score\n            }\n            cumulativeForHost {\n              reviewCount\n            }\n          }\n          providerReviewScore {\n            isDefault\n            providerId\n            trendingScore {\n              past14DaysUplift\n              past30DaysUplift\n            }\n            cumulative {\n              maxScore\n              reviewCount\n              score\n            }\n            demographics {\n              allGuest {\n                id\n                scoreDistribution {\n                  id\n                  reviewCount\n                }\n                reviewCount\n                grades {\n                  id\n                  score\n                  cityAverage\n                  subGrades {\n                    score\n                    name\n                  }\n                }\n              }\n            }\n          }\n          thirdPartyReviewScore {\n            providerId\n            grades {\n              id\n              score\n            }\n          }\n        }\n        contentSummary(ContentInformationSummaryRequest: $ContentInformationSummaryRequest) {\n          propertyId\n          displayName\n          defaultName\n          localeName\n          accommodation {\n            accommodationType\n            accommodationName\n          }\n          propertyType\n          address {\n            address1\n            address2\n            countryCode\n            area {\n              id\n              name\n            }\n            city {\n              id\n              name\n            }\n            country {\n              id\n              name\n            }\n            postalCode\n            stateInfo {\n              id\n            }\n          }\n          awardsAndAccolades {\n            goldCircleAward {\n              year\n            }\n            advanceGuaranteeProgram {\n              logo\n              description\n            }\n          }\n          remarks {\n            renovationInfo {\n              year\n              renovationType\n            }\n          }\n          hasHostExperience\n          geoInfo {\n            latitude\n            longitude\n          }\n          rating\n          asqType\n          asqInfos {\n            asqTypeId\n          }\n        }\n        contentEngagement {\n          peopleLooking\n          todayBooking\n        }\n        contentHighlights(ContentHighlightsRequest: $ContentHighlightsRequest) {\n          favoriteFeatures {\n            category\n            id\n            images {\n              id\n              urls {\n                key\n                value\n              }\n            }\n            name\n            symbol\n            tooltip\n          }\n          locationHighlightMessage {\n            title\n          }\n          locationHighlights {\n            distanceKm\n            highlightType\n            message\n          }\n          locations {\n            tooltip\n            symbol\n            name\n            images {\n              id\n              urls {\n                key\n                value\n              }\n            }\n          }\n          atfPropertyHighlights {\n            id\n            name\n            symbol\n            icon\n            category\n            images {\n              id\n              urls {\n                key\n                value\n              }\n            }\n            tooltip\n          }\n        }\n        contentLocalInformation(ContentLocalInformationRequest: $ContentLocalInformationRequest) {\n          walkablePlaces {\n            title\n            totalCount\n            description\n            walkableCategories {\n              categoryName\n              totalCount\n              topPlaces {\n                name\n                distanceInKm\n                images {\n                  urls {\n                    value\n                  }\n                }\n                landMarkGroup {\n                  name\n                  sortOrder\n                }\n              }\n            }\n          }\n          nearbyProperties {\n            categoryName\n            categorySymbol\n            id\n            places {\n              abbr\n              distanceInKm\n              duration\n              durationIcon\n              geoInfo {\n                latitude\n                longitude\n                obfuscatedLat\n                obfuscatedLong\n              }\n              images {\n                urls {\n                  value\n                  key\n                }\n                id\n              }\n              landmarkId\n              name\n              typeId\n              typeName\n            }\n          }\n          cuisines {\n            id\n            images {\n              urls {\n                value\n                key\n              }\n              id\n            }\n            name\n            restaurants {\n              cuisinesOffered\n              distance\n              id\n              name\n            }\n          }\n          locationSubscore {\n            airportScore\n            poiScore\n            transportationScore\n          }\n          nearbyPlaces {\n            abbr\n            distanceInKm\n            duration\n            durationIcon\n            geoInfo {\n              latitude\n              longitude\n              obfuscatedLat\n              obfuscatedLong\n            }\n            images {\n              urls {\n                value\n                key\n              }\n              id\n            }\n            landmarkId\n            name\n            typeId\n            typeName\n            landMarkGroup {\n              name\n              sortOrder\n            }\n          }\n          nearbyShops {\n            abbr\n            distanceInKm\n            duration\n            durationIcon\n            geoInfo {\n              latitude\n              longitude\n              obfuscatedLat\n              obfuscatedLong\n            }\n            images {\n              urls {\n                value\n                key\n              }\n              id\n            }\n            landmarkId\n            name\n            typeId\n            typeName\n          }\n          popularLandmarkNumber\n          topPlaces {\n            abbr\n            distanceInKm\n            duration\n            durationIcon\n            geoInfo {\n              latitude\n              longitude\n              obfuscatedLat\n              obfuscatedLong\n            }\n            images {\n              urls {\n                value\n                key\n              }\n              id\n            }\n            landmarkId\n            name\n            typeId\n            typeName\n            landMarkGroup {\n              name\n              sortOrder\n            }\n          }\n        }\n        contentInformation(ContentInformationRequest: $ContentInformationRequest) {\n          usefulInfoGroups {\n            id\n            usefulInfo {\n              id\n              description\n            }\n          }\n          certificate {\n            name\n            imageUrl\n            description\n          }\n          staffVaccinationInfo {\n            details\n            status\n          }\n          messaging {\n            responsiveRate\n            isAllowedPreBooking\n          }\n          description {\n            short\n          }\n          notes {\n            criticalNotes\n          }\n          sustainabilityInfo {\n            isSustainableTravel\n            practiceCategories {\n              categoryId\n              categoryName\n              practices {\n                practiceId\n                practiceName\n              }\n            }\n          }\n        }\n        contentFeatures(ContentFeaturesRequest: $ContentFeaturesRequest) {\n          featureGroups {\n            features {\n              available\n              featureName\n              featureNameLocalizationList {\n                locale\n                value\n              }\n              id\n              order\n              symbol\n              images {\n                id\n                urls {\n                  key\n                  value\n                }\n                groupId\n                groupEntityId\n                typeId\n                uploadedDate\n                providerId\n                caption\n                highResolutionSizes\n              }\n            }\n            id\n            name\n            order\n            symbol\n          }\n          hotelFacilities {\n            id\n            name\n          }\n          summary {\n            chineseFriendly\n            staycationFacilityIds {\n              activities\n              drinkingAndDining\n              sportAndEntertainment\n              wellness\n            }\n            hygienePlusFacilities {\n              healthAndMedical\n              safetyFeature\n              preventiveEquipment\n            }\n          }\n          facilityHighlights {\n            facilityId\n            facilityName\n            images {\n              id\n              urls {\n                key\n                value\n              }\n              groupId\n              groupEntityId\n              typeId\n              uploadedDate\n              providerId\n              caption\n              highResolutionSizes\n            }\n          }\n        }\n        hostProfile {\n          displayName\n          picture\n          averageReviewScore\n          totalReviews\n          hostLevel\n          responseRate\n          responseTimeSeconds\n          properties {\n            id\n            bookings\n            reviewAvg\n            reviewCount\n          }\n        }\n      }\n      metaLab(PriceStreamMetaLabRequest: $PriceStreamMetaLabRequest) {\n        propertyAttributes {\n          attributeId\n          dataType\n          value\n          version\n        }\n      }\n    }\n  }\n}\n",
        }

    def check_response(self):
        page = 1
        self.json_data["variables"]["CitySearchRequest"]["searchRequest"]["page"][
            "pageNumber"
        ] = page
        while page < 20:
            response = requests.post(
                "https://www.agoda.com/graphql/search",
                headers=self.headers,
                json=self.json_data,
            )

            if response.status_code == 200:
                return response
                page += 2

            else:
                print("Denied")
                time.sleep(59)

    def get_data(self):
        dr = self.check_response()
        print("Response = OK")

        res = dr.json()["data"]["citySearch"]["properties"]
        for i in range(len(res)):
            prop_id = res[i]["propertyId"]

            self.json_detail_page["variables"]["PropertyDetailsRequest"][
                "propertyIds"
            ] = [prop_id]

            r = requests.post(
                "https://www.agoda.com/graphql/property",
                headers=self.headers,
                json=self.json_detail_page,
            )

            print(r, i, "inner response")

            # Content = r.json()["data"]["propertyDetailsSearch"]["propertyDetails"][0][
            #     "contentDetail"
            # ]
            # name = Content["contentSummary"]["displayName"]
            # add = Content["contentSummary"]["address"]["address1"]
            # desc = Content["contentInformation"]["description"]
            # facility = Content["contentFeatures"]["hotelFacilities"]
            # facility = list(filter(lambda ele: ele.get("name") != None, facility))
            # ttl_facility = ',\n'.join(item['name'] for item in facility)
            # item = {"Name":name,"Address":add,"Description":desc,"Facilities":ttl_facility}
            # d1.append(item)
            # print(d1)


a = Scraper()
a.get_data()

# df = pd.DataFrame(d1)
# df.to_excel("Agoda.xlsx",index=False)
