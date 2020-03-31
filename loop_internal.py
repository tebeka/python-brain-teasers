
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


iterable = range(5)  # range is the iterable
iterator = iter(iterable)  # extract iterator from iterable
while True:
    try:
        n = next(iterator)
        # Code inside "for" loop
        print(n, end=' ')
        n = 5  # Will be overridden by line 5 in next iteration
    except StopIteration:  # iterator signaled it's exhausted
        break
print()  # Code after "for" loop
