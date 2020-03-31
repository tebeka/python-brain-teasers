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


def get_attr(obj, name):
    """Emulate built in getattr"""
    if name in obj.__dict__:
        print(f'found {name} in obj')
        return obj.__dict__[name]

    if name in obj.__class__.__dict__:
        print(f'found {name} in class')
        return obj.__class__.__dict__[name]

    for cls in obj.__class__.__mro__:
        if name in cls.__dict__:
            print(f'found {name} in {cls.__name__}')
            return cls.__dict__[name]

    raise AttributeError(name)


class A:
    a = 1


class B(A):
    b = 2

    def __init__(self):
        self.c = 3


b = B()
get_attr(b, 'a')
get_attr(b, 'b')
get_attr(b, 'c')
