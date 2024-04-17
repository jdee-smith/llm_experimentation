example_sql = """SELECT
    RTS.*, TTS.target_value
FROM
    Historical.TTS TTS
LEFT JOIN
    Historical.RTS RTS
        ON TTS.item_id = RTS.item_id AND TTS.timestamp = RTS.timestamp
ORDER BY
    RTS.item_id ASC, RTS.timestamp ASC"""
