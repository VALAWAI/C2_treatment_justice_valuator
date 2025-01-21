#
# This file is part of the C2_treatment_justice_valuator distribution
# (https://github.com/VALAWAI/C2_treatment_justice_valuator).
# Copyright (c) 2022-2026 VALAWAI (https://valawai.eu/).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import math
import random
import unittest

from json_resources import load_treatment_json

from c2_treatment_justice_valuator.justice_valuator import JusticeValuator
from c2_treatment_justice_valuator.patient_status_criteria import PatientStatusCriteria
from c2_treatment_justice_valuator.treatment_payload import TreatmentAction, TreatmentPayload


class TestJusticeValuator(unittest.TestCase):
	"""Class to test the justice valuator
	"""

	def setUp(self):
		"""Create the valuator."""

		self.valuator = JusticeValuator(
				age_range_weight=0.03528796,
				ccd_weight=0.0459857,
				maca_weight=0.03875686,
				expected_survival_weight=0.03503524,
				frail_VIG_weight=0.02724042,
				clinical_risk_group_weight=0.04153011,
				has_social_support_weight=0.02813626,
				independence_at_admission_weight=0.05733978,
				independence_instrumental_activities_weight=0.0619622,
				has_advance_directives_weight=0.02465476,
				is_competent_weight=0.05090684,
				has_been_informed_weight=0.03400722,
				is_coerced_weight=0.03652449,
				has_cognitive_impairment_weight=0.0595146,
				has_emocional_pain_weight=0.00456752,
				discomfort_degree_weight=0.00560229,
				cpr_weight=0.00130002,
				transplant_weight=0.05353632,
				icu_weight=0.05003441,
				nimv_weight=0.05594059,
				vasoactive_drugs_weight=0.06292382,
				dialysis_weight=0.0513848,
				simple_clinical_trial_weight=0.02967249,
				medium_clinical_trial_weight=0.05018696,
				advanced_clinical_trial_weight=0.00760488,
				palliative_surgery_weight=0.04114605,
				cure_surgery_weight=0.00921742
			)


	def test_align_justice(self):
		"""Test calculate alignment for a treatment"""

		treatment = TreatmentPayload(**load_treatment_json())
		alignment = self.valuator.align_justice(treatment)
		assert math.isclose(alignment, 0.3092993), 'Unexpected treatment justice alignment value'


	def test_align_justice_for_treatment_with_empty_before_status(self):
		"""Test calculate alignment with empty before status treatment"""

		treatment = TreatmentPayload(**load_treatment_json())
		treatment.before_status = PatientStatusCriteria()
		treatment.actions = [TreatmentAction.CPR]
		alignment = self.valuator.align_justice(treatment)
		assert math.isclose(alignment, 0.00130002), 'Unexpected treatment justice alignment value'

	def test_align_justice_for_treatment_with_empty_before_status_and_all_actions(self):
		"""Test calculate alignment with an empty treatment"""

		treatment = TreatmentPayload(**load_treatment_json())
		treatment.before_status = PatientStatusCriteria()
		treatment.actions = []
		for action in TreatmentAction:

			treatment.actions.append(action)

		random.shuffle(treatment.actions)
		alignment = self.valuator.align_justice(treatment)
		assert math.isclose(alignment, 0.41294776), 'Unexpected treatment justice alignment value'

if __name__ == '__main__':
    unittest.main()
