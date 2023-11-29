#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (c) 2022-2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from pathlib import Path


def generate_dataset(num_samples):
    resources_dir = Path(__file__).parent.resolve().parent
    data_dir = resources_dir / 'data'
    dummy_cnn_dataset = data_dir / 'dummy_cnn.json'

    input = ' '.join(['test' for _ in range(10)])
    output = ' '.join(['test' for _ in range(10)])

    samples = []
    for _ in range(num_samples):
        samples.append({
            "input": input,
            "instruction": "Summarize the following news article:",
            "output": output
        })

    with open(dummy_cnn_dataset, 'w') as f:
        json.dump(samples, f)
    print('write to', dummy_cnn_dataset)

if __name__ == '__main__':
    generate_dataset(num_samples=50)
