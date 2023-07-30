package com.codingdojo.yiip.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import com.codingdojo.yiip.models.LoginUser;
import com.codingdojo.yiip.models.User;
import com.codingdojo.yiip.services.UserService;

@RestController
@CrossOrigin(origins = "http://localhost:3000")
public class UserController {

	@Autowired
	private UserService userService;

	@CrossOrigin(origins = "http://localhost:3000")
	@ResponseStatus(HttpStatus.OK)
	@GetMapping("/api/user")
	public ResponseEntity<List<User>> getAllUsers() {
		return new ResponseEntity<>(userService.getAllUsers(), HttpStatus.OK);
	}

	@CrossOrigin(origins = "http://localhost:3000")
	@ResponseStatus(HttpStatus.OK)
	@GetMapping("/api/user/{id}")
	public ResponseEntity<User> getOneUser(@PathVariable("id") Long id) {
		return new ResponseEntity<>(userService.getOneUserById(id), HttpStatus.OK);
	}

	@CrossOrigin(origins = "http://localhost:3000")
	@ResponseStatus(HttpStatus.OK)
	@PostMapping("/api/user/login")
	public ResponseEntity<User> loginUser(@RequestBody LoginUser loginUser) {

		User loggingInUser = userService.login(loginUser);

		if (loggingInUser != null) {
			return new ResponseEntity<>(loggingInUser, HttpStatus.OK);
		}

		return new ResponseEntity<>(loggingInUser, HttpStatus.BAD_REQUEST);
	}

	@CrossOrigin(origins = "http://localhost:3000")
	@ResponseStatus(HttpStatus.CREATED)
	@PostMapping("/api/user")
	public ResponseEntity<User> createUser(@RequestBody User newUser) {
		System.out.println(newUser.getPassword());
		System.out.println(newUser.getConfirmPassword());
		System.out.println(newUser.getEmail());
		return new ResponseEntity<>(userService.createUser(newUser), HttpStatus.CREATED);
	}

	@CrossOrigin(origins = "http://localhost:3000")
	@ResponseStatus(HttpStatus.OK)
	@DeleteMapping("/api/user/{id}")
	public void deleteUser(@PathVariable("id") Long id) {
		userService.deleteUser(id);
	}
}