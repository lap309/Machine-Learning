SELECT p.gender, SAFE_CAST(p.age as int64) as age, p.admissionweight,
       a.unabridgedhosplos, a.acutephysiologyscore, a.apachescore, a.actualhospitalmortality,
       av.heartrate, av.meanbp, av.creatinine, av.temperature, av.respiratoryrate,
       av.wbc, p.admissionheight
FROM `physionet-data.eicu_crd_demo.patient` p
INNER JOIN `physionet-data.eicu_crd_demo.apachepatientresult` a
ON p.patientunitstayid = a.patientunitstayid
INNER JOIN `physionet-data.eicu_crd_demo.apacheapsvar` av
ON p.patientunitstayid = av.patientunitstayid
WHERE apacheversion LIKE 'IVa'
