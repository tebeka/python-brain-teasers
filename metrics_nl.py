
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


from functools import wraps


def metrics(fn):
    ncalls = 0
    name = fn.__name__

    @wraps(fn)
    def wrapper(*args, **kw):
        nonlocal ncalls
        ncalls += 1
        print(f'{name} called {ncalls} times')

    return wrapper


@metrics
def inc(n):
    return n + 1


inc(3)
