# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .secret_resource_properties import SecretResourceProperties


class SimpleSecretResourceProperties(SecretResourceProperties):
    """Describes the properties of a generic secret resource where the value is
    stored with the secret resource.

    :param description: Description of the secret.
    :type description: str
    :param content_type: The type of the secret value. Currently this value is
     opaque to Service Fabric.
    :type content_type: str
    :param value: The value of the secret resource. When creating or updating
     the resource, value is required. Once created, the value can be retrieved
     using an explicit operation against the resource.
    :type value: str
    :param version: The version of the secret value. If must be unique and
     different for different value. Once set, the value of the version property
     cannot be changed.
    :type version: str
    :param kind: Constant filled by server.
    :type kind: str
    """

    _validation = {
        'version': {'required': True},
        'kind': {'required': True},
    }

    def __init__(self, version, description=None, content_type=None, value=None):
        super(SimpleSecretResourceProperties, self).__init__(description=description, content_type=content_type, value=value, version=version)
        self.kind = 'simple'
