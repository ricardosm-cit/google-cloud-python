# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# DO NOT EDIT! This is a generated sample ("Request",  "data_catalog_get_entry")

# To install the latest published package dependency, execute the following:
#   pip install google-cloud-datacatalog

# sample-metadata
#   title:
#   description: Get Entry
#   usage: python3 samples/v1beta1/data_catalog_get_entry.py [--project "[Google Cloud Project ID]"] [--location "[Google Cloud Location]"] [--entry_group_id "[Entry Group ID]"] [--entry_id "[Entry ID]"]
import sys

# [START data_catalog_get_entry]

from google.cloud import datacatalog_v1beta1
from google.cloud.datacatalog_v1beta1 import enums


def sample_get_entry(project, location, entry_group_id, entry_id):
    """
    Get Entry

    Args:
      project Your Google Cloud project ID
      location Google Cloud region, e.g. us-central1
      entry_group_id ID of the Entry Group of this entry
      entry_id ID of the Entry
    """

    client = datacatalog_v1beta1.DataCatalogClient()

    # project = '[Google Cloud Project ID]'
    # location = '[Google Cloud Location]'
    # entry_group_id = '[Entry Group ID]'
    # entry_id = '[Entry ID]'
    name = client.entry_path(project, location, f'@{entry_group_id}', entry_id)

    response = client.get_entry(name)
    entry = response
    print(u"Entry name: {}".format(entry.name))
    print(u"Entry type: {}".format(enums.EntryType(entry.type).name))
    print(u"Linked resource: {}".format(entry.linked_resource))


# [END data_catalog_get_entry]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=str, default="[Google Cloud Project ID]")
    parser.add_argument("--location", type=str, default="[Google Cloud Location]")
    parser.add_argument("--entry_group_id", type=str, default="[Entry Group ID]")
    parser.add_argument("--entry_id", type=str, default="[Entry ID]")
    args = parser.parse_args()

    sample_get_entry(args.project, args.location, args.entry_group_id, args.entry_id)


if __name__ == "__main__":
    main()
