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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.	If not, see <http://www.gnu.org/licenses/>.
#

import os

from treatment_payload import TreatmentPayload, TreatmentAction


class JusticeValuator:
	"""The component that ovtain the benificence value from a patient treatment.
	"""

	def __init__(self,
		age_range_weight:float = float(os.getenv('AGE_RANGE_WEIGHT',"0.03528796")),
		ccd_weight:float = float(os.getenv('CCD_WEIGHT',"0.0459857")),
		maca_weight:float = float(os.getenv('MACA_WEIGHT',"0.03875686")),
		expected_survival_weight:float = float(os.getenv('EXPECTED_SURVIVAL_WEIGHT',"0.03503524")),
		frail_VIG_weight:float = float(os.getenv('FRAIL_VIG_WEIGHT',"0.02724042")),
		clinical_risk_group_weight:float = float(os.getenv('CLINICAL_RISK_GROUP_WEIGHT',"0.04153011")),
		has_social_support_weight:float = float(os.getenv('HAS_SOCIAL_SUPPORT_WEIGHT',"0.02813626")),
		independence_at_admission_weight:float = float(os.getenv('INDEPENDENCE_AT_ADMISSION_WEIGHT',"0.05733978")),
		independence_instrumental_activities_weight:float = float(os.getenv('INDEPENDENCE_INSTRUMENTAL_ACTIVITIES_WEIGHT',"0.0619622")),
		has_advance_directives_weight:float = float(os.getenv('HAS_ADVANCE_DIRECTIVES_WEIGHT',"0.02465476")),
		is_competent_weight:float = float(os.getenv('IS_COMPETENT_WEIGHT',"0.05090684")),
		has_been_informed_weight:float = float(os.getenv('HAS_BEEN_INFORMED_WEIGHT',"0.03400722")),
		is_coerced_weight:float = float(os.getenv('IS_COERCED_WEIGHT',"0.03652449")),
		has_cognitive_impairment_weight:float = float(os.getenv('HAS_COGNITIVE_IMPAIRMENT_WEIGHT',"0.0595146")),
		has_emocional_pain_weight:float = float(os.getenv('HAS_EMOCIONAL_PAIN_WEIGHT',"0.00456752")),
		discomfort_degree_weight:float = float(os.getenv('DISCOMFORT_DEGREE_WEIGHT',"0.00560229")),
		cpr_weight:float = float(os.getenv('CPR_WEIGHT',"0.00130002")),
		transplant_weight:float = float(os.getenv('TRANSPLANT_WEIGHT',"0.05353632")),
		icu_weight:float = float(os.getenv('ICU_WEIGHT',"0.05003441")),
		mimv_weight:float = float(os.getenv('MIMV_WEIGHT',"0.05594059")),
		vasoactive_drugs_weight:float = float(os.getenv('VASOACTIVE_DRUGS_WEIGHT',"0.06292382")),
		dialysis_weight:float = float(os.getenv('DIALYSIS_WEIGHT',"0.0513848")),
		simple_clinical_trial_weight:float = float(os.getenv('SIMPLE_CLINICAL_TRIAL_WEIGHT',"0.02967249")),
		medium_clinical_trial_weight:float = float(os.getenv('MEDIUM_CLINICAL_TRIAL_WEIGHT',"0.05018696")),
		advanced_clinical_trial_weight:float = float(os.getenv('ADVANCED_CLINICAL_TRIAL_WEIGHT',"0.00760488")),
		paliative_surgery_weight:float = float(os.getenv('PALIATIVE_SURGERY_WEIGHT',"0.04114605")),
		cure_surgery_weight:float = float(os.getenv('CURE_SURGERY_WEIGHT',"0.00921742"))
		):
		"""Initialize the justice valuator

		Parameters
		----------
		age_range_weight: float
			The importance of the age range when calculate the justice value.
		ccd_weight: float
			The importance of the ccd when calculate the justice value.
		maca_weight: float
			The importance of the MACA when calculate the justice value.
		expected_survival_weight: float
			The importance of the expected survival when calculate the justice value.
		frail_VIG_weight: float
			The importance of the frail VIG when calculate the justice value.
		clinical_risk_group_weight: float
			The importance of the clinical risk group when calculate the justice value.
		has_social_support_weight: float
			The importance of the has social support_weight when calculate the justice value.
		independence_at_admission_weight: float
			The importance of the independence at admission weight when calculate the justice value.
		independence_instrumental_activities_weight: float
			The importance of the independence instrumental activities when calculate the justice value.
		has_advance_directives_weight: float
			The importance of the has advance directives when calculate the justice value.
		is_competent_weight: float
			The importance of the is competent when calculate the justice value.
		has_been_informed_weight: float
			The importance of the has been informed when calculate the justice value.
		is_coerced_weight: float
			The importance of the is coerced when calculate the justice value.
		has_cognitive_impairment_weight: float
			The importance of the has cognitive impairment when calculate the justice value.
		has_emocional_pain_weight: float
			The importance of the has emocional pain when calculate the justice value.
		discomfort_degree_weight: float
			The importance of the discomfort degree when calculate the justice value.
		cpr_weight: :float
			The importance of the CPR action when calculate the justice value.
		transplant_weight: :float
			The importance of the transplant action when calculate the justice value.
		icu_weight: :float
			The importance of the ICU action when calculate the justice value.
		mimv_weight: :float
			The importance of the MIMV action when calculate the justice value.
		vasoactive_drugs_weight: :float
			The importance of the vasoactive drugs action when calculate the justice value.
		dialysis_weight: :float
			The importance of the dialysis action when calculate the justice value.
		simple_clinical_trial_weight: :float
			The importance of the simple clinical trial action when calculate the justice value.
		medium_clinical_trial_weight: :float
			The importance of the medium clinical trial action when calculate the justice value.
		advanced_clinical_trial_weight: :float
			The importance of the advanced clinical trial action when calculate the justice value.
		paliative_surgery_weight: :float
			The importance of the paliative surgery action when calculate the justice value.
		cure_surgery_weight: :float
			The importance of the cure surgery action when calculate the justice value.
		"""
		self.age_range_weight = age_range_weight
		self.ccd_weight = ccd_weight
		self.maca_weight = maca_weight
		self.expected_survival_weight = expected_survival_weight
		self.frail_VIG_weight = frail_VIG_weight
		self.clinical_risk_group_weight = clinical_risk_group_weight
		self.has_social_support_weight = has_social_support_weight
		self.independence_at_admission_weight = independence_at_admission_weight
		self.independence_instrumental_activities_weight = independence_instrumental_activities_weight
		self.has_advance_directives_weight = has_advance_directives_weight
		self.is_competent_weight = is_competent_weight
		self.has_been_informed_weight = has_been_informed_weight
		self.is_coerced_weight = is_coerced_weight
		self.has_cognitive_impairment_weight = has_cognitive_impairment_weight
		self.has_emocional_pain_weight = has_emocional_pain_weight
		self.discomfort_degree_weight = discomfort_degree_weight
		self.cpr_weigh = cpr_weigh
		self.transplant_weigh = transplant_weigh
		self.icu_weigh = icu_weigh
		self.mimv_weigh = mimv_weigh
		self.vasoactive_drugs_weigh = vasoactive_drugs_weigh
		self.dialysis_weigh = dialysis_weigh
		self.simple_clinical_trial_weigh = simple_clinical_trial_weigh
		self.medium_clinical_trial_weigh = medium_clinical_trial_weigh
		self.advanced_clinical_trial_weigh = advanced_clinical_trial_weigh
		self.paliative_surgery_weigh = paliative_surgery_weigh
		self.cure_surgery_weigh = cure_surgery_weigh


	def align_justice(self,treatment:TreatmentPayload):
		"""Calculate the alignemnt of a treatemnt with the justice value.

		Parameters
		----------
		treatment : Treatment
			The treatemnt to apply inot a patient

		Returns
		-------
		float
			The align,ment of the treatment with the justice value.
		"""

		alignment = 0.0

		alignment += self.age_range_weight * treatment.before_status.normalized_age_range()
		alignment += self.ccd_weight * treatment.before_status.normalized_ccd()
		alignment += self.maca_weight * treatment.before_status.normalized_maca()
		alignment += self.expected_survival_weight * treatment.before_status.normalized_expected_survival()
		alignment += self.frail_VIG_weight * treatment.before_status.normalized_frail_vig()
		alignment += self.clinical_risk_group_weight * treatment.before_status.normalized_clinical_risk_group()
		alignment += self.has_social_support_weight * treatment.before_status.normalized_has_social_support()
		alignment += self.independence_at_admission_weight * treatment.before_status.normalized_independence_at_admission()
		alignment += self.independence_instrumental_activities_weight * treatment.before_status.normalized_independence_instrumental_activities()
		alignment += self.has_advance_directives_weight * treatment.before_status.normalized_has_advance_directives()
		alignment += self.is_competent_weight * treatment.before_status.normalized_is_competent()
		alignment += self.has_been_informed_weight * treatment.before_status.normalized_has_been_informed()
		alignment += self.is_coerced_weight * treatment.before_status.normalized_is_coerced()
		alignment += self.has_cognitive_impairment_weight * treatment.before_status.normalized_has_cognitive_impairment()
		alignment += self.has_emocional_pain_weight * treatment.before_status.normalized_has_emocional_pain()
		alignment += self.discomfort_degree_weight * treatment.before_status.normalized_discomfort_degree()

		if TreatmentAction.CPR in treatment.actions:
			alignment += self.cpr_weigh
			
		if TreatmentAction.TRANSPLANT in treatment.actions:
			alignment += self.transplant_weigh
			
		if TreatmentAction.ICU in treatment.actions:
			alignment += self.icu_weigh
			
		if TreatmentAction.MIMV in treatment.actions:
			alignment += self.mimv_weigh
		
		if TreatmentAction.VASOACTIVE_DRUGS in treatment.actions:
			alignment += self.vasoactive_drugs_weigh
			
		if TreatmentAction.DIALYSIS in treatment.actions:
			alignment += self.dialysis_weigh
			
		if TreatmentAction.SIMPLE_CLINICAL_TRIAL in treatment.actions:
			alignment += self.simple_clinical_trial_weigh
			
		if TreatmentAction.MEDIUM_CLINICAL_TRIAL in treatment.actions:
			alignment += self.medium_clinical_trial_weigh
			
		if TreatmentAction.ADVANCED_CLINICAL_TRIAL in treatment.actions:
			alignment += self.advanced_clinical_trial_weigh
			
		if TreatmentAction.PALIATIVE_SURGERY in treatment.actions:
			
			alignment += self.paliative_surgery_weigh
			
		if TreatmentAction.CURE_SURGERY in treatment.actions:
			alignment += self.cure_surgery_weigh

		return alignment
