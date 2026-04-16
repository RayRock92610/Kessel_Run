export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).end();
  const { email } = req.body;
  // TODO: Send to Sheets/Mailgun ($0.001/email)
  console.log('Waitlist:', email);
  res.status(200).json({ success: true });
}
