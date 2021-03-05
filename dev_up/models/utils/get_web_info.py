from typing import Optional

from pydantic import BaseModel


class UtilsGetWebInfoResponseIpInfoOrganization(BaseModel):
    name: Optional[str]
    as_code: Optional[str]
    as_name: Optional[str]


class UtilsGetWebInfoResponseIpInfoConnection(BaseModel):
    status: Optional[str]
    mobile_network: Optional[bool]
    direct_connection: Optional[bool]
    proxy: Optional[bool]
    web_server: Optional[bool]


class UtilsGetWebInfoResponseIpInfo(BaseModel):
    address: Optional[str]
    ip: Optional[str]
    dns: Optional[str]
    offset: Optional[int]
    organization: Optional[UtilsGetWebInfoResponseIpInfoOrganization]
    connection: Optional[UtilsGetWebInfoResponseIpInfoConnection]


class UtilsGetWebInfoResponseIpGeoRegionInfo(BaseModel):
    name: Optional[str]
    code: Optional[str]


class UtilsGetWebInfoResponseIpGeoCoordinates(BaseModel):
    latitude: Optional[float]
    longitude: Optional[float]


class UtilsGetWebInfoResponseIpGeo(BaseModel):
    city: Optional[str]
    currency: Optional[str]
    zip: Optional[str]
    timezone: Optional[str]

    continent: Optional[UtilsGetWebInfoResponseIpGeoRegionInfo]
    country: Optional[UtilsGetWebInfoResponseIpGeoRegionInfo]
    region: Optional[UtilsGetWebInfoResponseIpGeoRegionInfo]
    coordinates: Optional[UtilsGetWebInfoResponseIpGeoCoordinates]


class UtilsGetWebInfoResponse(BaseModel):
    ip_info: UtilsGetWebInfoResponseIpInfo
    ip_geo: UtilsGetWebInfoResponseIpGeo


class UtilsGetWebInfo(BaseModel):
    response: UtilsGetWebInfoResponse
