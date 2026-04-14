import { useState, useEffect } from 'react'
import axios from 'axios'
import { ShieldCheck, TrendingUp, MapPin, Box, AlertTriangle, Zap } from 'lucide-react'
import './App.css'

function App() {
  const [shield, setShield] = useState(null)
  const [hype, setHype] = useState(null)
  const [allocation, setAllocation] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // This is the bridge between your React Frontend and Python Backend
    const fetchData = async () => {
      try {
        const shieldRes = await axios.get('http://127.0.0.1:8000/api/shield')
        const hypeRes = await axios.get('http://127.0.0.1:8000/api/hype')
        const allocRes = await axios.get('http://127.0.0.1:8000/api/allocation')
        
        setShield(shieldRes.data)
        setHype(hypeRes.data)
        setAllocation(allocRes.data)
        setLoading(false)
      } catch (error) {
        console.error("Connection Error: Is the Python server running?", error)
      }
    }
    fetchData()
  }, [])

  if (loading) return <div className="loading">Initiating Pulse AI Engine...</div>

  return (
    <div className="dashboard">
      <header className="header">
        <div className="logo-area">
          <Zap size={32} color="#00ffcc" />
          <h1>NIKE <span className="highlight">PULSE</span></h1>
        </div>
        <div className="status-badge">🟢 AI Engine Live</div>
      </header>

      <div className="grid-container">
        {/* Layer 1: Biometric Shield */}
        <div className="card shield-card">
          <div className="card-header">
            <ShieldCheck size={24} color="#00ffcc" />
            <h2>Biometric Shield</h2>
          </div>
          <div className="stats-row">
            <div className="stat-box">
              <h3>Total Requests</h3>
              <p className="number">{shield.total_requests}</p>
            </div>
            <div className="stat-box danger">
              <h3>Bots Blocked</h3>
              <p className="number">{shield.bots_blocked}</p>
            </div>
            <div className="stat-box success">
              <h3>Humans Verified</h3>
              <p className="number">{shield.humans_verified}</p>
            </div>
          </div>
          <div className="logs">
            <p className="log-title">Recent Intercepts:</p>
            {shield.recent_blocks.map((block, i) => (
              <div key={i} className="log-entry">
                <AlertTriangle size={14} color="#ff4444" />
                <span>[{block.id}] Blocked in {block.location} - {block.reason}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Layer 2: NLP Senses */}
        <div className="card hype-card">
          <div className="card-header">
            <TrendingUp size={24} color="#ff00cc" />
            <h2>Localized Hype (VADER)</h2>
          </div>
          <div className="leaderboard">
            {hype.leaderboard.map((item, i) => (
              <div key={i} className="leaderboard-item">
                <div className="rank">#{item.rank}</div>
                <div className="geo">
                  <MapPin size={16} /> {item.region}
                </div>
                <div className="score">{item.score}</div>
              </div>
            ))}
          </div>
        </div>

        {/* Layer 3: Prophet Allocation */}
        <div className="card allocation-card">
          <div className="card-header">
            <Box size={24} color="#ffff00" />
            <h2>Smart Allocation</h2>
          </div>
          <div className="target-area">
            <h3>Target: {allocation.target_region}</h3>
            <p className="product">Product: {allocation.shoe_model}</p>
          </div>
          
          <div className="allocation-math">
            <div className="math-step">
              <span>Baseline (Prophet):</span>
              <span className="value">{allocation.baseline_prediction} pairs</span>
            </div>
            <div className="math-step">
              <span>Hype Multiplier (VADER):</span>
              <span className="value modifier">x {allocation.hype_multiplier}</span>
            </div>
            <div className="divider"></div>
            <div className="math-step final">
              <span>Final Approved Shipment:</span>
              <span className="value highlight-text">{allocation.final_approved_allocation} pairs</span>
            </div>
            <div className="delta-badge">
              {allocation.delta} vs Baseline
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App