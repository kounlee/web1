import pymongo

m = {
    "문제":"a",
    "보기":"b",
    "답":"c",
}

conn = pymongo.MongoClient("localhost",27017)
db = conn.problem
col = db.members

col.insert(m)