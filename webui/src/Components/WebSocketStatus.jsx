import React from 'react';
import './WebSocketStatus.scss';

function WebSocketStatus({ wsIsOpen, wsIsAuthenticated, wsURI, wsIsRecovering }) {
  if (wsIsOpen && !wsIsAuthenticated) {
    return (
      <div className="WebSocketStatus">
        Authenticating against {wsURI}
      </div>
    );
  }

  if (wsIsRecovering) {
    return (
      <div className="WebSocketStatus">
        Reconnecting to {wsURI}
      </div>
    );
  }

  if (wsIsOpen) {
    return (
      <div className="WebSocketStatus">
        Receiving real time updates from {wsURI}
      </div>
    );
  }

  return null;
}

export default WebSocketStatus;
