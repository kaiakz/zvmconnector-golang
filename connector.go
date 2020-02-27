package zvmconnector

import (
	"time"
)

// Connect provide some function
type Connect interface {
	Fetch(fn string, apiArgs string) string
	Close()
}

// NewClient create a RestClient or SDKSocketClient
func NewClient(ip string, port uint16, timeout time.Duration, isRest bool) (Connect, error) {
	if isRest {
		return NewSDKSocketClient(ip, port, timeout)
	} else {
		return NewSDKSocketClient(ip, port, timeout)
	}
}
