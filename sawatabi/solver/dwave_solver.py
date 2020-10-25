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
from dwave.system.composites import EmbeddingComposite
from dwave.system.samplers import DWaveSampler

import sawatabi.constants as constants
from sawatabi.model.physical_model import PhysicalModel
from sawatabi.solver.abstract_solver import AbstractSolver


class DWaveSolver(AbstractSolver):
    def __init__(self):
        super().__init__()

    def solve(self, model, seed=None, chain_strength=2, num_reads=1000):
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

        solver = EmbeddingComposite(DWaveSampler())
        sampleset = solver.sample(bqm, chain_strength=chain_strength, num_reads=num_reads)

        return sampleset