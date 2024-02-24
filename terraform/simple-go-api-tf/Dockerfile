##
## Build
##
FROM golang:latest AS build

WORKDIR /app

COPY go.mod ./
COPY go.sum ./
RUN go mod download

COPY *.go ./

RUN go build -o /main

##
## Deploy
##
FROM golang:latest


WORKDIR /

COPY --from=build /main /main

EXPOSE 8080

# USER nonroot:nonroot

ENTRYPOINT ["/main"]
