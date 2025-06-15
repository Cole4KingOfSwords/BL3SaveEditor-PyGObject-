source .venv/bin/activate
if test -e "python/Protobufs/OakSave_pb2.py"; then
  echo 1
else
  cd python/Protobufs
  protoc --python_out=. OakSave.proto
  cd ..
  cd ..
fi
cd python
python3 main.py