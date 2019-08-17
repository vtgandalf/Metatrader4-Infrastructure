PROTOS := $(shell find $(protos) -name '*.proto')
PATH_SERVER_PROTOS = server/messages
PATH_META_CLIENT_PROTOS = meta_client/messages
PATH_USER_CLIENT_PROTOS = user_client/messages
PATH_PROTOS = protos

all: clean python csharp

.PHONY: all

clean:
	rm $(PATH_SERVER_PROTOS)/*.py
	rm $(PATH_USER_CLIENT_PROTOS)/*.cs
	rm $(PATH_META_CLIENT_PROTOS)/*.py

python:
	protoc -I=/usr/local/include --proto_path=$(PATH_PROTOS) --python_out=$(PATH_SERVER_PROTOS) $(PROTOS)
	protoc -I=/usr/local/include --proto_path=$(PATH_PROTOS) --python_out=$(PATH_META_CLIENT_PROTOS) $(PROTOS)

csharp:
	protoc -I=/usr/local/include --proto_path=$(PATH_PROTOS) --csharp_out=$(PATH_USER_CLIENT_PROTOS) $(PROTOS)
