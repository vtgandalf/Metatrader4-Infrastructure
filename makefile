PROTOS := $(shell find $(protos) -name '*.proto')
PATH_SERVER_PROTOS = server/messages
PATH_META_CLIENT_PROTOS = meta_client/messages
PATH_USER_CLIENT_PROTOS = user_client/messages
PATH_TESTING_PROTOS = examples/messages
PATH_PROTOS = protos

all: python csharp

.PHONY: all

clean:
	rm $(PATH_SERVER_PROTOS)/*.py
	rm $(PATH_USER_CLIENT_PROTOS)/*.cs
	rm $(PATH_META_CLIENT_PROTOS)/*.py
	rm $(PATH_TESTING_PROTOS)/*.py

python:
	python -m grpc_tools.protoc -I=/usr/local/include --proto_path=$(PATH_PROTOS) --python_out=$(PATH_SERVER_PROTOS) --grpc_python_out=$(PATH_SERVER_PROTOS) $(PROTOS) 
	python -m grpc_tools.protoc -I=/usr/local/include --proto_path=$(PATH_PROTOS) --python_out=$(PATH_META_CLIENT_PROTOS) --grpc_python_out=$(PATH_META_CLIENT_PROTOS) $(PROTOS)
	python -m grpc_tools.protoc -I=/usr/local/include --proto_path=$(PATH_PROTOS) --python_out=$(PATH_TESTING_PROTOS) --grpc_python_out=$(PATH_TESTING_PROTOS) $(PROTOS)

csharp:
	protoc -I=/usr/local/include --proto_path=$(PATH_PROTOS) --csharp_out=$(PATH_USER_CLIENT_PROTOS) $(PROTOS)
