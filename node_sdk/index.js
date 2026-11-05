/**
 * InsightUIUX™ — Universal Node.js / CommonJS SDK (`node_sdk/index.js`)
 * Powered by InsightCore (`insightCoreIO + insightCoreAI`).
 */

class InsightUIUXClient {
  constructor(config = {}) {
    this.baseUrl = config.baseUrl || process.env.INSIGHT_UIUX_URL || 'http://127.0.0.1:4023/api/uiux';
  }

  async _request(path, method = 'GET', body = null) {
    const opts = {
      method,
      headers: {
        'Content-Type': 'application/json',
        'X-Origin-Platform': 'InsightUIUX-NodeSDK'
      }
    };
    if (body !== null) opts.body = JSON.stringify(body);
    const res = await fetch(`${this.baseUrl}${path}`, opts);
    if (!res.ok) throw new Error(`InsightUIUX HTTP ${res.status}: ${res.statusText}`);
    return await res.json();
  }

  async getStatus() {
    return await this._request('/status', 'GET');
  }

  async getTokens() {
    return await this._request('/tokens', 'GET');
  }

  async getPenpotTokens(title = 'InsightUIUX Penpot Component') {
    return await this._request(`/penpot-tokens?title=${encodeURIComponent(title)}`, 'GET');
  }

  async getPatterns(patternId = 'linear_issue_table_and_command_palette') {
    return await this._request(`/patterns?pattern_id=${encodeURIComponent(patternId)}`, 'GET');
  }

  async execute(payload = {}) {
    return await this._request('/execute', 'POST', payload);
  }
}

module.exports = { InsightUIUXClient };
