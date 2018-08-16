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

from msrest.serialization import Model


class UpgradeDomainInfo(Model):
    """Information about an upgrade domain.

    :param name: The name of the upgrade domain
    :type name: str
    :param state: The state of the upgrade domain. Possible values include:
     'Invalid', 'Pending', 'InProgress', 'Completed'
    :type state: str or ~azure.servicefabric.models.UpgradeDomainState
    """

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'state': {'key': 'State', 'type': 'str'},
    }

    def __init__(self, name=None, state=None):
        super(UpgradeDomainInfo, self).__init__()
        self.name = name
        self.state = state
