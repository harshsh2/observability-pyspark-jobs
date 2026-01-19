.PHONY: login build push image

REGION ?= ap-south-1
ACCOUNT ?= 568130295144
REGISTRY := $(ACCOUNT).dkr.ecr.$(REGION).amazonaws.com
ECR_REPOSITORY ?= ondc-prod-prod-ondc-images
IMAGE_NAME ?= ondc-no-workbench-validations

ifndef VERSION
$(error VERSION is not set. Run make with VERSION=<value>, e.g. `make build VERSION=1.0.0`)
endif

IMAGE_TAG := v$(VERSION)
IMAGE := $(REGISTRY)/$(ECR_REPOSITORY):$(IMAGE_NAME)-$(IMAGE_TAG)

login:
	aws ecr get-login-password --region $(REGION) | docker login --username AWS --password-stdin $(REGISTRY)/$(ECR_REPOSITORY)

build:
	docker build --platform=linux/amd64 -t $(IMAGE) .

push: login build
	docker push $(IMAGE)

image:
	@echo $(IMAGE)
