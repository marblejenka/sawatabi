# Copyright 2020 Kotaro Terada, Shingo Furuyama, Junya Usui, and Kazuki Ono
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

import dimod
import neal

import sawatabi.constants as constants
from sawatabi.model.physical_model import PhysicalModel
from sawatabi.solver.abstract_solver import AbstractSolver


class LocalSolver(AbstractSolver):
    def __init__(self, exact=False):
        self._exact = exact

    def solve(self, model):
        self._check_argument_type("model", model, PhysicalModel)

        if (
            len(model._interactions[constants.INTERACTION_LINEAR]) == 0
            and len(model._interactions[constants.INTERACTION_QUADRATIC]) == 0
        ):
            raise ValueError("Model cannot be empty.")

        # Signs for BQM are opposite from our definition.
        # - BQM:  H =   sum( J_{ij} * x_i * x_j ) + sum( h_{i} * x_i )
        # - Ours: H = - sum( J_{ij} * x_i * x_j ) - sum( h_{i} * x_i )
        linear, quadratic = {}, {}
        for k, v in model._interactions[constants.INTERACTION_LINEAR].items():
            linear[k] = -1.0 * v
        for k, v in model._interactions[constants.INTERACTION_QUADRATIC].items():
            quadratic[k] = -1.0 * v

        if model.get_mtype() == constants.MODEL_ISING:
            vartype = dimod.SPIN
        elif model.get_mtype() == constants.MODEL_QUBO:
            vartype = dimod.BINARY
        bqm = dimod.BinaryQuadraticModel(linear, quadratic, model._offset, vartype)

        if self._exact:
            # dimod's brute force solver
            sampleset = dimod.ExactSolver().sample(bqm)

        else:
            # Simulated annealing (SA)
            sampler = neal.SimulatedAnnealingSampler()
            sampleset = sampler.sample(bqm)

        return sampleset