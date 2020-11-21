# Copyright 2020 Kotaro Terada
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sawatabi


def _create_ising_model():
    # Optimal solution of this ising model:
    #   - x[1][0] and x[1][1]: -1
    #   - The others: +1
    #   - Energy = -16.0
    model = sawatabi.model.LogicalModel(mtype="ising")

    # print("\nSet shape to (1, 2)")
    x = model.variables("x", shape=(1, 2))
    model.add_interaction(x[0, 0], coefficient=1.0)
    model.add_interaction((x[0, 0], x[0, 1]), coefficient=1.0)
    # print(model)

    # print("\nAdd shape by (1, 0)")
    x = model.append("x", shape=(1, 0))
    model.add_interaction((x[0, 1], x[1, 0]), coefficient=-2.0)
    model.add_interaction((x[1, 0], x[1, 1]), coefficient=3.0)
    # print(model)

    # print("\nAdd shape by (1, 0)")
    x = model.append("x", shape=(1, 0))
    model.add_interaction((x[1, 1], x[2, 0]), coefficient=-4.0)
    model.add_interaction((x[2, 0], x[2, 1]), coefficient=5.0)
    # print(model)

    # print("\nPhysical model")
    physical = model.to_physical()
    # print(physical)

    return physical


def _create_qubo_model():
    # Optimal solution of this qubo model:
    #   - Only one of the variables: 1
    #   - The others: 0
    #   - Energy = -1.0
    model = sawatabi.model.LogicalModel(mtype="qubo")

    # print("\nOne-hot constraint for an array of (4,)")
    a = model.variables("a", shape=(4,))
    # model.add_interaction(a[0], coefficient=10.0)
    model.n_hot_constraint(a, n=1)
    # print(model)

    # print("\nPhysical model")
    physical = model.to_physical()
    # print(physical)

    return physical


def _print_resultset(resultset):
    print("\nresultset")
    print(resultset)
    print("\nresultset.info")
    print(resultset.info)
    print("\nresultset.variables")
    print(resultset.variables)
    print("\nresultset.record")
    print(resultset.record)
    print("\nresultset.vartype:")
    print(resultset.vartype)
    print("\nresultset.first:")
    print(resultset.first)
    print("\nresultset.samples():")
    print([sample for sample in resultset.samples()])
