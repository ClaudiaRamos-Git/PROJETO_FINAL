-- ============================================================
-- QUERY 01 — Distribuição de salários por departamento e cargo
-- ============================================================

SELECT 
    e.SALARY SALARIO_BASE,
    d.DEPARTMENT_NAME DEPARTAMENTO,
    j.JOB_TITLE CARGO
FROM HR.EMPLOYEES e
LEFT JOIN HR.JOBS j
    ON e.JOB_ID = j.JOB_ID
LEFT JOIN HR.DEPARTMENTS d
    ON d.DEPARTMENT_ID = e.DEPARTMENT_ID
ORDER BY
    SALARIO_BASE DESC;


-- ============================================================
-- QUERY 02 — Salários e distribuição geográfica (Cidade, Estado ou País)
-- ============================================================
-- Versão inicial, sem filtro:

SELECT 
    e.FIRST_NAME FUNCIONARIO,
    r.REGION_NAME REGIAO,
    l.STREET_ADDRESS LOCALIZACAO,
    e.SALARY SALARIO
FROM HR.DEPARTMENTS d
LEFT JOIN HR.EMPLOYEES e
    ON e.DEPARTMENT_ID = d.DEPARTMENT_ID
LEFT JOIN HR.LOCATIONS l
    ON d.LOCATION_ID = l.LOCATION_ID
LEFT JOIN HR.COUNTRIES c
    ON l.COUNTRY_ID = c.COUNTRY_ID
LEFT JOIN HR.REGIONS r
    ON r.REGION_ID = c.REGION_ID;


-- ------------------------------------------------------------
-- QUERY 02 — Versão final, com filtro WHERE simples aplicado
-- Foi proposto aplicar um filtro utilizando um comando WHERE
-- simples, por exemplo:
--   WHERE SALARY > ...
--   WHERE DEPARTMENT_ID IS NOT NULL
--   WHERE REGION_NAME IS NOT NULL
-- ------------------------------------------------------------

SELECT 
    e.FIRST_NAME FUNCIONARIO,
    r.REGION_NAME REGIAO,
    l.STREET_ADDRESS LOCALIZACAO,
    d.DEPARTMENT_ID DEPARTAMENTO,
    e.SALARY SALARIO
FROM HR.DEPARTMENTS d
LEFT JOIN HR.EMPLOYEES e
    ON e.DEPARTMENT_ID = d.DEPARTMENT_ID
LEFT JOIN HR.LOCATIONS l
    ON d.LOCATION_ID = l.LOCATION_ID
LEFT JOIN HR.COUNTRIES c
    ON l.COUNTRY_ID = c.COUNTRY_ID
LEFT JOIN HR.REGIONS r
    ON r.REGION_ID = c.REGION_ID
WHERE d.DEPARTMENT_ID IS NOT NULL
  AND r.REGION_NAME IS NOT NULL;
