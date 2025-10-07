import { useState } from 'react';
import './Signup.css'; // Add this line

export default function Signup() {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    firstName: '',
    lastName: '',
    petName: '',
    petAge: '',
    species: '',
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Form submitted:', formData);
  };

  return (
    <div className="signup-container">
      <form className="signup-form" onSubmit={handleSubmit}>
        <h2>Create Your Pet Profile</h2>

        <input name="username" placeholder="Username" onChange={handleChange} required />
        <input name="password" type="password" placeholder="Password" onChange={handleChange} required />
        <input name="firstName" placeholder="First Name" onChange={handleChange} />
        <input name="lastName" placeholder="Last Name" onChange={handleChange} />
        <input name="petName" placeholder="Pet Name" onChange={handleChange} required />
        <input name="petAge" type="number" placeholder="Pet Age" onChange={handleChange} />
        
        <select name="species" onChange={handleChange} required>
          <option value="">Select Species</option>
          <option value="cat">Cat</option>
          <option value="dog">Dog</option>
        </select>

        <button type="submit">Sign Up</button>
      </form>
    </div>
  );
}
