package com.codingdojo.yiip.services;

import java.util.List;
import java.util.Optional;

import org.mindrot.jbcrypt.BCrypt;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.codingdojo.yiip.models.LoginUser;
import com.codingdojo.yiip.models.User;
import com.codingdojo.yiip.repositories.UserRepository;

@Service
public class UserService {

	@Autowired
	private UserRepository userRepo;

	public User createUser(User newUser){

		Optional<User> potentialUser = userRepo.findByEmail(newUser.getEmail());
		String passwordEntered = newUser.getPassword();

		if (potentialUser.isPresent()) {
			System.out.println("potential user is present");
			return null;
		}

		if (!newUser.getPassword().equals(newUser.getConfirmPassword())) {
			System.out.println("Bad Password");
			System.out.println(newUser.getPassword());
			System.out.println(newUser.getConfirmPassword());
			return null;
		}

		String hashed = BCrypt.hashpw(passwordEntered, BCrypt.gensalt());

		newUser.setPassword(hashed);
		return userRepo.save(newUser);
	}
	
	public User login(LoginUser loginUser) {

		Optional<User> potentialUser = userRepo.findByEmail(loginUser.getEmail());

		if (potentialUser.isEmpty()) {
			return null;
		}

		User userFromDb = potentialUser.get();

		if (!BCrypt.checkpw(loginUser.getPassword(), userFromDb.getPassword())) {
			return null;
		}
		
		return userFromDb;
	}

	public List<User> getAllUsers() {
		return userRepo.findAll();
	}

	public User getOneUserById(Long id) {
		Optional<User> oneUser = userRepo.findById(id);

		if (oneUser.isPresent()) {
			return oneUser.get();
		}

		return null;
	}

	public void deleteUser(Long id) {
		userRepo.deleteById(id);
	}
}
