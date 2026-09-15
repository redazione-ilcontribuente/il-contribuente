export default function VerifyBadge({ html }) {
  return (
    <div className="verify-badge">
      <div
        className="verify-badge-inner"
        dangerouslySetInnerHTML={{ __html: html }}
      />
    </div>
  )
}
