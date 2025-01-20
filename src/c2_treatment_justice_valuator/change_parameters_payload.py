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


from pydantic import BaseModel, Field


class ChangeParametersPayload(BaseModel):
	"""The payload of the message to change the parameters of teh component."""

	age_range_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the age range when calculate the justice value.")
	ccd_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the ccd when calculate the justice value.")
	maca_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the MACA when calculate the justice value.")
	expected_survival_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the expected survival when calculate the justice value.")
	frail_VIG_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the frail VIG when calculate the justice value.")
	clinical_risk_group_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the clinical risk group when calculate the justice value.")
	has_social_support_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the has social support_weight when calculate the justice value.")
	independence_at_admission_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the independence at admission weight when calculate the justice value.")
	independence_instrumental_activities_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the independence instrumental activities when calculate the justice value.")
	has_advance_directives_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the has advance directives when calculate the justice value.")
	is_competent_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the is competent when calculate the justice value.")
	has_been_informed_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the has been informed when calculate the justice value.")
	is_coerced_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the is coerced when calculate the justice value.")
	has_cognitive_impairment_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the has cognitive impairment when calculate the justice value.")
	has_emocional_pain_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the has emocional pain when calculate the justice value.")
	discomfort_degree_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the discomfort degree when calculate the justice value.")
	cpr_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the CPR action when calculate the justice value.")
	transplant_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the transplant action when calculate the justice value.")
	icu_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the ICU action when calculate the justice value.")
	mimv_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the MIMV action when calculate the justice value.")
	vasoactive_drugs_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the vasoactive drugs action when calculate the justice value.")
	dialysis_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the dialysis action when calculate the justice value.")
	simple_clinical_trial_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the simple clinical trial action when calculate the justice value.")
	medium_clinical_trial_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the medium clinical trial action when calculate the justice value.")
	advanced_clinical_trial_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the advanced clinical trial action when calculate the justice value.")
	paliative_surgery_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the paliative surgery action when calculate the justice value.")
	cure_surgery_weight: float | None = Field(default=None, ge=0.0, le=1.0, title="The importance of the cure surgery action when calculate the justice value.")