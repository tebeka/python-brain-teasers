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


s1 = '\x61'  # \x - 2 digits
print(s1)  # a

s2 = '\u2122'  # \u - 4 digits (8482 in hex)
print(s2)  # ™

s3 = '\U00002122'  # \U - 8 digits
print(s3)  # ™

s4 = '\N{trade mark sign}'
print(s4)  # ™
