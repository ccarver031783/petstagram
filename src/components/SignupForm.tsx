// src/components/SignupForm.tsx
import { useState } from 'react';

export default function SignupForm() {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    firstName: '',
    lastName: '',
    petName: '',
    petAge: '',
    species: '',
  });

  const [error, setError] = useState('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    // Basic validation
    if (!formData.username || formData.password.length < 6 || !formData.petName || !formData.species) {
      setError('Please fill out all required fields and use a secure password.');
      return;
    }

    try {
      const response = await fetch('http://localhost:8000/api/signup/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      if (!response.ok) throw new Error('Signup failed');
      const result = await response.json();
      console.log('Signup successful:', result);
      setError('');
    } catch (err) {
      setError('Signup failed. Please try again.');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="username" placeholder="Username" value={formData.username} onChange={handleChange} required />
      <input name="password" type="password" placeholder="Password" value={formData.password} onChange={handleChange} required />
      <input name="firstName" placeholder="First Name" value={formData.firstName} onChange={handleChange} />
      <input name="lastName" placeholder="Last Name" value={formData.lastName} onChange={handleChange} />
      <input name="petName" placeholder="Pet Name" value={formData.petName} onChange={handleChange} required />
      <input name="petAge" type="number" placeholder="Pet Age" value={formData.petAge} onChange={handleChange} />
      <select name="species" value={formData.species} onChange={handleChange} required>
        <option value="">Select Species</option>
        <option value="cat">Cat</option>
        <option value="dog">Dog</option>
      </select>

      {error && <div style={{ color: 'red' }}>{error}</div>}
      <button type="submit">Sign Up</button>
    </form>
  );
}
