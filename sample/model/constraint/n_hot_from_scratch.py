#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2021 Kotaro Terada
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

import platform
import sys

import sawatabi


def _print_utf8(model):
    """
    Util function for Windows (GitHub Actions)
    """
    if platform.system() == "Windows":
        sys.stdout.buffer.write(str(model).encode("utf-8"))
    else:
        print(model)


def n_hot_from_scratch_2_of_1_qubo(solver):
    print("\n=== N-hot from scratch (2 of 1) qubo ===")
    model = sawatabi.model.LogicalModel(mtype="qubo")
    x = model.variables("x", shape=(2,))

    # quadratic
    model.add_interaction((x[0], x[1]), coefficient=-2.0)
    # linear
    coeff = 1.0 - 2 * 1
    model.add_interaction(x[0], coefficient=-coeff)
    model.add_interaction(x[1], coefficient=-coeff)
    _print_utf8(model)

    sampleset = solver.solve(model.to_physical())
    print(sampleset)


def n_hot_from_scratch_3_of_1_qubo(solver):
    print("\n=== N-hot from scratch (3 of 1) qubo ===")
    model = sawatabi.model.LogicalModel(mtype="qubo")
    x = model.variables("x", shape=(3,))

    # quadratic
    model.add_interaction((x[0], x[1]), coefficient=-2.0)
    model.add_interaction((x[0], x[2]), coefficient=-2.0)
    model.add_interaction((x[1], x[2]), coefficient=-2.0)
    # linear
    coeff = 1.0 - 2 * 1
    model.add_interaction(x[0], coefficient=-coeff)
    model.add_interaction(x[1], coefficient=-coeff)
    model.add_interaction(x[2], coefficient=-coeff)
    _print_utf8(model)

    sampleset = solver.solve(model.to_physical())
    print(sampleset)


def n_hot_from_scratch_3_of_2_qubo(solver):
    print("\n=== N-hot from scratch (3 of 2) qubo ===")
    model = sawatabi.model.LogicalModel(mtype="qubo")
    x = model.variables("x", shape=(3,))

    # quadratic
    model.add_interaction((x[0], x[1]), coefficient=-2.0)
    model.add_interaction((x[0], x[2]), coefficient=-2.0)
    model.add_interaction((x[1], x[2]), coefficient=-2.0)
    # linear
    coeff = 1.0 - 2 * 2
    model.add_interaction(x[0], coefficient=-coeff)
    model.add_interaction(x[1], coefficient=-coeff)
    model.add_interaction(x[2], coefficient=-coeff)
    _print_utf8(model)

    sampleset = solver.solve(model.to_physical())
    print(sampleset)


def n_hot_from_scratch_4_of_1_qubo(solver):
    print("\n=== N-hot from scratch (4 of 1) qubo ===")
    model = sawatabi.model.LogicalModel(mtype="qubo")
    x = model.variables("x", shape=(4,))

    # quadratic
    model.add_interaction((x[0], x[1]), coefficient=-2.0)
    model.add_interaction((x[0], x[2]), coefficient=-2.0)
    model.add_interaction((x[0], x[3]), coefficient=-2.0)
    model.add_interaction((x[1], x[2]), coefficient=-2.0)
    model.add_interaction((x[1], x[3]), coefficient=-2.0)
    model.add_interaction((x[2], x[3]), coefficient=-2.0)
    # linear
    coeff = 1.0 - 2 * 1
    model.add_interaction(x[0], coefficient=-coeff)
    model.add_interaction(x[1], coefficient=-coeff)
    model.add_interaction(x[2], coefficient=-coeff)
    model.add_interaction(x[3], coefficient=-coeff)
    _print_utf8(model)

    sampleset = solver.solve(model.to_physical())
    print(sampleset)


def n_hot_from_scratch_4_of_2_qubo(solver):
    print("\n=== N-hot from scratch (4 of 2) qubo ===")
    model = sawatabi.model.LogicalModel(mtype="qubo")
    x = model.variables("x", shape=(4,))

    # quadratic
    model.add_interaction((x[0], x[1]), coefficient=-2.0)
    model.add_interaction((x[0], x[2]), coefficient=-2.0)
    model.add_interaction((x[0], x[3]), coefficient=-2.0)
    model.add_interaction((x[1], x[2]), coefficient=-2.0)
    model.add_interaction((x[1], x[3]), coefficient=-2.0)
    model.add_interaction((x[2], x[3]), coefficient=-2.0)
    # linear
    coeff = 1.0 - 2 * 2
    model.add_interaction(x[0], coefficient=-coeff)
    model.add_interaction(x[1], coefficient=-coeff)
    model.add_interaction(x[2], coefficient=-coeff)
    model.add_interaction(x[3], coefficient=-coeff)
    _print_utf8(model)

    sampleset = solver.solve(model.to_physical())
    print(sampleset)


def n_hot_from_scratch_2_of_1_ising(solver):
    print("\n=== N-hot from scratch (2 of 1) ising ===")
    model = sawatabi.model.LogicalModel(mtype="ising")
    x = model.variables("x", shape=(2,))

    # quadratic
    model.add_interaction((x[0], x[1]), coefficient=-2.0)
    # linear
    coeff = 2.0 * (2 - 2 * 1)
    model.add_interaction(x[0], coefficient=-coeff)
    model.add_interaction(x[1], coefficient=-coeff)
    _print_utf8(model)

    sampleset = solver.solve(model.to_physical())
    print(sampleset)


def n_hot_from_scratch_3_of_1_ising(solver):
    print("\n=== N-hot from scratch (3 of 1) ising ===")
    model = sawatabi.model.LogicalModel(mtype="ising")
    x = model.variables("x", shape=(3,))

    # quadratic
    model.add_interaction((x[0], x[1]), coefficient=-2.0)
    model.add_interaction((x[0], x[2]), coefficient=-2.0)
    model.add_interaction((x[1], x[2]), coefficient=-2.0)
    # linear
    coeff = 2.0 * (3 - 2 * 1)
    model.add_interaction(x[0], coefficient=-coeff)
    model.add_interaction(x[1], coefficient=-coeff)
    model.add_interaction(x[2], coefficient=-coeff)
    _print_utf8(model)

    sampleset = solver.solve(model.to_physical())
    print(sampleset)


def n_hot_from_scratch_3_of_2_ising(solver):
    print("\n=== N-hot from scratch (3 of 2) ising ===")
    model = sawatabi.model.LogicalModel(mtype="ising")
    x = model.variables("x", shape=(3,))

    # quadratic
    model.add_interaction((x[0], x[1]), coefficient=-2.0)
    model.add_interaction((x[0], x[2]), coefficient=-2.0)
    model.add_interaction((x[1], x[2]), coefficient=-2.0)
    # linear
    coeff = 2.0 * (3 - 2 * 2)
    model.add_interaction(x[0], coefficient=-coeff)
    model.add_interaction(x[1], coefficient=-coeff)
    model.add_interaction(x[2], coefficient=-coeff)
    _print_utf8(model)

    sampleset = solver.solve(model.to_physical())
    print(sampleset)


def n_hot_from_scratch_4_of_1_ising(solver):
    print("\n=== N-hot from scratch (4 of 1) ising ===")
    model = sawatabi.model.LogicalModel(mtype="ising")
    x = model.variables("x", shape=(4,))

    # quadratic
    model.add_interaction((x[0], x[1]), coefficient=-2.0)
    model.add_interaction((x[0], x[2]), coefficient=-2.0)
    model.add_interaction((x[0], x[3]), coefficient=-2.0)
    model.add_interaction((x[1], x[2]), coefficient=-2.0)
    model.add_interaction((x[1], x[3]), coefficient=-2.0)
    model.add_interaction((x[2], x[3]), coefficient=-2.0)
    # linear
    coeff = 2.0 * (4 - 2 * 1)
    model.add_interaction(x[0], coefficient=-coeff)
    model.add_interaction(x[1], coefficient=-coeff)
    model.add_interaction(x[2], coefficient=-coeff)
    model.add_interaction(x[3], coefficient=-coeff)
    _print_utf8(model)

    sampleset = solver.solve(model.to_physical())
    print(sampleset)


def n_hot_from_scratch_4_of_2_ising(solver):
    print("\n=== N-hot from scratch (4 of 1) ising ===")
    model = sawatabi.model.LogicalModel(mtype="ising")
    x = model.variables("x", shape=(4,))

    # quadratic
    model.add_interaction((x[0], x[1]), coefficient=-2.0)
    model.add_interaction((x[0], x[2]), coefficient=-2.0)
    model.add_interaction((x[0], x[3]), coefficient=-2.0)
    model.add_interaction((x[1], x[2]), coefficient=-2.0)
    model.add_interaction((x[1], x[3]), coefficient=-2.0)
    model.add_interaction((x[2], x[3]), coefficient=-2.0)
    # linear
    coeff = 2.0 * (4 - 2 * 2)
    model.add_interaction(x[0], coefficient=-coeff)
    model.add_interaction(x[1], coefficient=-coeff)
    model.add_interaction(x[2], coefficient=-coeff)
    model.add_interaction(x[3], coefficient=-coeff)
    _print_utf8(model)

    sampleset = solver.solve(model.to_physical())
    print(sampleset)


def main():
    solver = sawatabi.solver.LocalSolver(exact=True)

    n_hot_from_scratch_2_of_1_qubo(solver)
    n_hot_from_scratch_3_of_1_qubo(solver)
    n_hot_from_scratch_3_of_2_qubo(solver)
    n_hot_from_scratch_4_of_1_qubo(solver)
    n_hot_from_scratch_4_of_2_qubo(solver)

    n_hot_from_scratch_2_of_1_ising(solver)
    n_hot_from_scratch_3_of_1_ising(solver)
    n_hot_from_scratch_3_of_2_ising(solver)
    n_hot_from_scratch_4_of_1_ising(solver)
    n_hot_from_scratch_4_of_2_ising(solver)


if __name__ == "__main__":
    main()
