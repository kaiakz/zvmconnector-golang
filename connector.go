package zvmconnector

import (
	"time"
)

// Connect provide some function
type Connect interface {
	Fetch(apiName string, apiArgs []string, apiKArgs map[string]interface{}) Response
	Close()
}

// NewConnector create a RestClient or SDKSocketClient
func NewConnector(ip string, port uint16, timeout time.Duration, isRest bool) (Connect, error) {
	if isRest {
		return NewRestClient(ip, port, timeout, "")
	}
	return NewSDKSocketClient(ip, port, timeout)
}
