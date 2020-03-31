
# Copyright 2020 Miki Tebeka <miki@353solutions.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


scale = 1.1


def make_mul(n):
    def mul(val):
        out = val * n * scale  # <1>
        return out  # <2>
    return mul


mul7 = make_mul(7)
print(mul7(3))  # 23.1
