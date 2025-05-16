SET QUOTED_IDENTIFIER ON;

SET ANSI_NULLS ON;
GO

CREATE OR ALTER FUNCTION dbo.f_pasien_regis(@rt_tgl1 date
                                          , @rt_tgl2 date) RETURNS TABLE AS RETURN
(
    SELECT isnull(sum(CASE
                          WHEN w.NOREG IS NULL
                          THEN 1
                          ELSE 0
                      END), 0) AS rj
         , isnull(sum(CASE
                          WHEN w.NOREG IS NULL
                          THEN 0
                          ELSE 1
                      END), 0) AS ri
         , FORMAT(@rt_tgl1, 'd MMMM yyyy', 'id-ID') AS tgl1
         , FORMAT(@rt_tgl2, 'd MMMM yyyy', 'id-ID') AS tgl2
    FROM   BNA.dbo.REGPAS AS r(NOLOCK)
           INNER JOIN BNA.dbo.REGDR AS d(NOLOCK) ON d.NOREG = r.NOREG
           INNER JOIN BNA.dbo.PASIEN AS p(NOLOCK) ON p.NOPASIEN = r.NOPASIEN
           LEFT OUTER JOIN BNA.dbo.REGRWI AS w(NOLOCK) ON w.NOREG = r.NOREG
    WHERE  cast(r.TGLREG AS date) BETWEEN @rt_tgl1 AND @rt_tgl2
);
GO