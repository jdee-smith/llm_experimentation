example_sql = """WITH CTE AS (
    SELECT
        RTS.*,
        TTS.sales,
        IMD.city,
        IMD.state
    FROM
        TTS
    LEFT JOIN
        RTS ON TTS.store = RTS.store AND TTS.week = RTS.week
    LEFT JOIN
        IMD ON TTS.store = IMD.store
    WHERE
        TTS.scenario = 0
    ORDER BY
        RTS.store ASC, RTS.week ASC
)

SELECT
    *
FROM CTE"""
