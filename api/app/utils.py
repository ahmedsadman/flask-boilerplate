def commit_or_rollback(session):
    try:
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise
